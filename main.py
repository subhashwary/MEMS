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

        # Close previous PSU connection if any
        try:
            if psu:
                psu.close()
        except:
            pass

        try:

            psu = None
            response = ""

            # Try common baud rates
            for baud in [9600, 19200, 38400, 57600]:

                try:

                    print(f"\nTrying PSU baudrate: {baud}")

                    candidate = PowerSupply(
                        port=com_port,
                        baudrate=baud,
                        timeout=2
                    )

                    print("IDN  =", candidate.query("*IDN?"))
                    print("VSET =", candidate.query("VSET1?"))
                    print("ISET =", candidate.query("ISET1?"))

                    response = candidate.query("*IDN?")

                    # If we get any valid response, keep this connection
                    if response:

                        psu = candidate

                        print("\n================================")
                        print("PSU CONNECTED SUCCESSFULLY")
                        print("PORT:", com_port)
                        print("BAUDRATE:", baud)
                        print("ID:", response)
                        print("================================\n")

                        return jsonify({
                            "status": "connected",
                            "baudrate": baud,
                            "id": response
                        })

                    else:
                        candidate.close()

                except Exception as e:

                    print(f"Failed at {baud}: {e}")

            # If all baud rates fail
            psu = None

            return jsonify({
                "status": "error",
                "message": "No response from PSU on any baud rate"
            }), 500

        except Exception as e:

            psu = None

            return jsonify({
                "status": "error",
                "message": str(e)
            }), 500


@app.route('/psu_test')
def psu_test():

    global psu

    try:

        print("Sending VSET1:2.00")
        psu.write("VSET1:2.00")

        time.sleep(1)

        print("Sending ISET1:0.10")
        psu.write("ISET1:0.10")

        time.sleep(1)

        print("Sending OUT1")
        psu.write("OUT1")

        return "Commands Sent"

    except Exception as e:

        return str(e)


@app.route('/psu_test')
def psu_test():

    global psu

    try:
        psu.write("VSET1:1.00")
        time.sleep(1)

        psu.write("ISET1:0.10")
        time.sleep(1)

        psu.write("OUT1")

        return "Commands Sent"

    except Exception as e:
        return str(e)

# =========================================================
# LIVE DATA API
# =========================================================
@app.route('/data')
def data():
    # Simulated pressure reading (replace with real sensor data)
    system_state["pressure"] = round(random.uniform(20, 100), 2)
