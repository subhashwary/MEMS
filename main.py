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

    try:

        print(f"Setting Voltage = {voltage}")
        print(f"Setting Current = {current}")

        psu.set_voltage(voltage)
        psu.set_current(current)

        # Verify PSU accepted values
        print("VERIFY VSET =", psu.query("VSET1?"))
        print("VERIFY ISET =", psu.query("ISET1?"))

        psu.output_on()

        print("PSU OUTPUT ON")

        return jsonify({
            "status": "PSU started",
            "voltage": voltage,
            "current": current
        })

    except Exception as e:

        print("PSU START ERROR:", e)

        return jsonify({"error": str(e)}), 500


@app.route('/psu/stop', methods=['POST'])
def stop_psu():

    if psu:
        try:
            psu.output_off()

            system_state["dmm_running"] = False
            system_state["dmm_voltage"] = 0.0

        except Exception as e:
            return jsonify({"error": str(e)}), 500

    return jsonify({"status": "PSU stopped"})

# =========================================================
# NEW ROUTE
# =========================================================
@app.route('/psu/set', methods=['POST'])
def set_psu():

    global psu

    data = request.json

    voltage = float(data["voltage"])
    current = float(data["current"])

    try:

        psu.set_voltage(voltage)
        psu.set_current(current)

        print(f"SET V={voltage}")
        print(f"SET I={current}")

        return jsonify({
            "status": "updated"
        })

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500

# =========================================================
# SAVE AUTO MODE CONFIGURATION
# =========================================================
@app.route('/config', methods=['POST'])
def save_config():
    data = request.json or {}

    system_state["config"] = {
        "initial_off": int(data.get("initial_off", 5)),
        "on_time": int(data.get("on_time", 5)),
        "off_time": int(data.get("off_time", 5)),
        "cycles": int(data.get("cycles", 10))
    }

    system_state["cycle_start"] = time.time()

    return jsonify({
        "status": "Configuration saved",
        "config": system_state["config"]
    })


# =========================================================
# DOWNLOAD CSV
# =========================================================
@app.route('/download')
def download():
    return send_file(CSV_FILE, as_attachment=True)


# =========================================================
# GET INSTRUMENT IDS
# =========================================================
@app.route('/id')
def get_ids():
    return jsonify({
        "psu_id": psu.idn() if psu else "Not Connected",
        "dmm_id": dmm.idn() if dmm else "Not Connected"
    })


# =========================================================
# GET AVAILABLE COM PORTS
# =========================================================
@app.route('/ports')
def get_ports():

    ports = serial.tools.list_ports.comports()

    port_list = []

    for port in ports:
        port_list.append({
            "device": port.device,
            "description": port.description
        })

    return jsonify(port_list)



# =========================================================
# CONNECT DMM
# =========================================================
@app.route('/connect_dmm', methods=['POST'])
def connect_dmm():

    global dmm

    data = request.json

    com_port = data.get("port")

    BAUDRATES = [9600, 19200, 38400, 57600, 115200]

    # -----------------------------------------
    # CLOSE OLD CONNECTION FIRST
    # -----------------------------------------
    try:
        if dmm:
            dmm.close()
            dmm = None
    except:
        pass

    # -----------------------------------------
    # TRY DIFFERENT BAUDRATES
    # -----------------------------------------
    for baud in BAUDRATES:

        test_dmm = None

        try:

            print(f"\nTrying baudrate: {baud}")

            test_dmm = Multimeter(
                port=com_port,
                baudrate=baud,
                timeout=2
            )

            # give instrument time
            time.sleep(1)

            response = test_dmm.idn()

            print("RAW ID RESPONSE:", response)

            # ---------------------------------
            # VALID RESPONSE CHECK
            # ---------------------------------
            if response and len(response) > 3:

                dmm = test_dmm

                print("\n================================")
                print("DMM CONNECTED SUCCESSFULLY")
                print("PORT:", com_port)
                print("BAUDRATE:", baud)
                print("DMM ID:", response)
                print("================================\n")

                return jsonify({
                    "status": "connected",
                    "id": response,
                    "baudrate": baud
                })

            else:

                print("Invalid response")

                test_dmm.close()

        except Exception as e:

            print(f"FAILED at {baud}: {e}")

            # IMPORTANT
            try:
                if test_dmm:
                    test_dmm.close()
            except:
                pass

    # -----------------------------------------
    # IF ALL BAUDRATES FAIL
    # -----------------------------------------
    dmm = None

    return jsonify({
        "status": "error",
        "message": "Could not connect to DMM"
    }), 500


# =========================================================
# MAIN
# =========================================================
if __name__ == '__main__':
    app.run(
    debug=False,
    threaded=True
)
