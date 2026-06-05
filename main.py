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
try:
    psu = PowerSupply(
        port="COM5",
        baudrate=9600,
        timeout=2
    )

    print("================================")
    print("PSU CONNECTED")
    print("PORT = COM5")
    print("================================")

except Exception as e:

    print("PSU CONNECTION FAILED")
    print(e)

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


