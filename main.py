from flask import Flask, jsonify, request, render_template, send_file
import random
import time
import serial.tools.list_ports
import pyvisa

rm = pyvisa.ResourceManager()

psu = rm.open_resource("ASRL5::INSTR")

from threading import Lock

serial_lock = Lock()

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

        response = psu.idn()

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


# =========================================================
# LIVE DATA API
# =========================================================
@app.route('/data')
def data():
    # Simulated pressure reading (replace with real sensor data)
    system_state["pressure"] = round(random.uniform(20, 100), 2)

    # -----------------------------------------------------
    # AUTO MODE LOGIC
    # -----------------------------------------------------
    if system_state["mode"] == "auto":
        cfg = system_state["config"]
        elapsed = time.time() - system_state["cycle_start"]

        cycle_period = cfg["on_time"] + cfg["off_time"]

        if elapsed < cfg["initial_off"]:
            system_state["dmm_running"] = False
        else:
            adjusted = elapsed - cfg["initial_off"]
            position = adjusted % cycle_period
            system_state["dmm_running"] = position < cfg["on_time"]

    # -----------------------------------------------------
    # DMM VOLTAGE READING
    # -----------------------------------------------------
    if system_state["dmm_running"]:
        if dmm:
            try:
                reading = dmm.measure_voltage()

                if isinstance(reading, (int, float)):
                    system_state["dmm_voltage"] = reading
            except Exception as e:
                print("DMM read error:", e)
                system_state["dmm_voltage"] = 0.0
        else:
            # Simulation mode if DMM not connected
            system_state["dmm_voltage"] = round(random.uniform(0, 10), 3)
    else:
        system_state["dmm_voltage"] = 0.0

    # -----------------------------------------------------
    # PSU READINGS
    # -----------------------------------------------------
    if psu:
        try:
            system_state["psu_voltage"] = float(psu.get_voltage())
            system_state["psu_current"] = float(psu.get_current())
        except Exception as e:
            print("PSU read error:", e)

    # -----------------------------------------------------
    # LOG DATA TO CSV
    # -----------------------------------------------------
    log_data(
        system_state["pressure"],
        system_state["dmm_voltage"],
        system_state["psu_voltage"],
        system_state["psu_current"],
        system_state["mode"]
    )

    return jsonify(system_state)


# =========================================================
# MODE CONTROL
# =========================================================
@app.route('/mode', methods=['POST'])
def set_mode():
    mode = request.json.get("mode")

    if mode in ["manual", "auto"]:
        system_state["mode"] = mode
        system_state["cycle_start"] = time.time()
        return jsonify({"status": f"{mode} mode activated"})

    return jsonify({"error": "Invalid mode"}), 400


# =========================================================
# DMM CONTROL
# =========================================================
@app.route('/dmm/start', methods=['POST'])
def start_dmm():
    if system_state["mode"] != "manual":
        return jsonify({"error": "Auto mode active"}), 403

    system_state["dmm_running"] = True
    return jsonify({"status": "DMM started"})


@app.route('/dmm/stop', methods=['POST'])
def stop_dmm():
    if system_state["mode"] != "manual":
        return jsonify({"error": "Auto mode active"}), 403

    system_state["dmm_running"] = False
    return jsonify({"status": "DMM stopped"})


# =========================================================
# POWER SUPPLY CONTROL
# =========================================================
@app.route('/psu/start', methods=['POST'])
def start_psu():

    global psu

    data = request.json or {}

    voltage = float(data.get("voltage", 0))
    current = float(data.get("current", 0))

    if not psu:
        return jsonify({"error": "PSU not connected"}), 500
