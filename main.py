from flask import Flask, jsonify, request, render_template, send_file
import random
import time
import serial.tools.list_ports

from threading import Lock

serial_lock = Lock()

psu_lock = Lock()

from instrument import PowerSupply, Multimeter
from logger import initialize_csv, log_data, CSV_FILE

app = Flask(__name__)

# =========================================================
# INITIALIZATION
# =========================================================
initialize_csv()

# Connect to instruments (replace COM ports with your actual ports)
psu = None

dmm = None

# =========================================================
# GLOBAL SYSTEM STATE
# =========================================================
system_state = {
    "mode": "manual",
    "dmm_running": False,
    "dmm_voltage": 0.0,
    "pressure": 0.0,
    "psu_voltage": 0.0,
    "psu_current": 0.0,
    "cycle_start": time.time(),
    "config": {
        "initial_off": 5,
        "on_time": 5,
        "off_time": 5,
        "cycles": 10
    }
}


# =========================================================
# WEB PAGE
# =========================================================
@app.route('/')
def index():
    return render_template('index.html')



@app.route('/status')
def status():

    return jsonify({
        "psu_connected": psu is not None,
        "dmm_connected": dmm is not None
    })


@app.route('/connect_psu', methods=['POST'])
def connect_psu():

    global psu

    data = request.json
    com_port = data.get("port")

    with psu_lock:
        
        try:

            if psu:
                psu.close()

        except:
            pass

        try:

            psu = PowerSupply(
                port=com_port,
                baudrate=9600,
                timeout=2
            )

            print("\nTesting PSU...")

            print("IDN =", psu.query("*IDN?"))
            print("VSET =", psu.query("VSET1?"))
            print("ISET =", psu.query("ISET1?"))

            response = psu.idn()

            print("VSET =", psu.query("VSET1?"))
            print("ISET =", psu.query("ISET1?"))

            print("\n========================")
            print("PSU CONNECTED")
            print("PORT:", com_port)
            print("ID:", response)
            print("========================\n")

            return jsonify({
                "status": "connected",
                "id": response
            })

        except Exception as e:

            psu = None

            return jsonify({
                "status": "error",
                "message": str(e)
            }), 500
