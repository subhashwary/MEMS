from flask import Flask, jsonify, request, render_template, send_file
import random
import time
import serial.tools.list_ports
import re

def parse_value(x):
    try:
        if x is None:
            return 0.0
        x = str(x)
        
        # extract number from: "1.998V", "0.700A", "+0.282E+1"
        match = re.search(r"[-+]?\d*\.?\d+(?:[eE][-+]?\d+)?", x)
        return float(match.group()) if match else 0.0
    except:
        return 0.0
    
    global psu

    if not psu:
        return "PSU not connected"

    try:
        with psu_lock:

            cmd_v = f"VSET1:{voltage:.3f}\r\n"
            cmd_i = f"ISET1:{current:.3f}\r\n"

            psu.write(cmd_v)
            time.sleep(0.1)

            psu.write(cmd_i)
            time.sleep(0.1)

            psu.write("OUT1\r\n")

        return "OK"

    except Exception as e:
        return str(e)

from threading import Lock

serial_lock = Lock()

psu_lock = Lock()
psu_busy = False

from instrument import PowerSupply, Multimeter
from logger import initialize_csv, log_data, CSV_FILE

app = Flask(__name__)

# INITIALIZATION
initialize_csv()

# Connect to instruments (replace COM ports with your actual ports)
psu = None

dmm = None

# GLOBAL SYSTEM STATE
system_state = {
    "mode": "manual",
    "dmm_running": False,
    "dmm_voltage": 0.0,
    "pressure": 0.0,

    "psu_voltage": 0.0,
    "psu_current": 0.0,
    "psu_output": False,

    "cycle_start": time.time(),

    # 🔴 ADD THIS LINE
    "last_psu_read": 0,

    "config": {
        "initial_off": 5,
        "on_time": 5,
        "off_time": 5,
        "cycles": 10
    }
}

# WEB PAGE
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
                        # timeout=2
                    )

                    idn  = candidate.query("*IDN?")
                    vset = candidate.query("VSET1?")
                    iset = candidate.query("ISET1?")

                    print("IDN  =", idn)
                    print("VSET =", vset)
                    print("ISET =", iset)

                    if not idn and not vset and not iset:
                        print("No PSU response")
                        candidate.close()
                        continue

                    try:

                        candidate.write("VSET1:2.00")
                        time.sleep(0.5)

                        candidate.write("ISET1:0.10")
                        time.sleep(0.5)

                        check_v = candidate.query("VSET1?")
                        check_i = candidate.query("ISET1?")

                        print("VERIFY V =", check_v)
                        print("VERIFY I =", check_i)

                        print("PORT =", com_port)
                        print("BAUD =", baud)
                        print("OPEN =", candidate.ser.is_open)

                        psu = candidate

                        system_state["psu_output"] = False
                        system_state["psu_voltage"] = 0.0
                        system_state["psu_current"] = 0.0

                        print("\n================================")
                        print("PSU CONNECTED SUCCESSFULLY")
                        print("PORT:", com_port)
                        print("BAUDRATE:", baud)
                        print("================================\n")

                        return jsonify({
                            "status": "connected",
                            "baudrate": baud,
                            "id": f"PSU Connected @ {baud}"
                        })

                    except Exception as e:

                        print("PSU TEST FAILED:", e)

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

    if not psu:
        return "PSU not connected"

    try:

        psu.write("VSET1:2.00")
        time.sleep(1)

        psu.write("ISET1:0.10")
        time.sleep(1)

        psu.write("OUT1")

        return "Commands Sent"

    except Exception as e:

        return str(e)

@app.route('/psu_debug')    
def psu_debug():

    global psu

    if not psu:
        return "No PSU"

    try:

        print("VSET1? =", psu.query("VSET1?"))
        print("ISET1? =", psu.query("ISET1?"))
        print("VOUT1? =", psu.query("VOUT1?"))
        print("IOUT1? =", psu.query("IOUT1?"))

        return "Done"

    except Exception as e:
        return str(e)

# LIVE DATA API
@app.route('/data')
def data():

    global psu_busy, psu

    # Simulated pressure reading
    system_state["pressure"] = round(random.uniform(20, 100), 2)

    # AUTO MODE LOGIC
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

    # DMM READING
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
            system_state["dmm_voltage"] = round(random.uniform(0, 10), 3)
    else:
        system_state["dmm_voltage"] = 0.0

    # PSU READINGS (FIXED LOCATION)
    PSU_READ_INTERVAL = 1

    last_psu_read = system_state.get("last_psu_read", 0)

    if (
        psu
        and not psu_busy
        and (time.time() - last_psu_read > PSU_READ_INTERVAL)
    ):

        try:

            with psu_lock:

                if system_state["psu_output"]:

                    v = psu.query("VOUT1?")
                    i = psu.query("IOUT1?")

                else:

                    v = "0"
                    i = "0"

            print("PSU V =", v)
            print("PSU I =", i)

            if not v or not i:

                print("WARNING: PSU returned empty response")

            else:

                system_state["psu_voltage"] = parse_value(v)
                system_state["psu_current"] = parse_value(i)

                system_state["last_psu_read"] = time.time()

        except Exception as e:

            print("PSU read error:", e)

            try:
                psu.close()
            except:
                pass

            psu = None

    # LOG DATA
    log_data(
        system_state["pressure"],
        system_state["dmm_voltage"],
        system_state["psu_voltage"],
        system_state["psu_current"],
        system_state["mode"]
    )

    return jsonify(system_state)

# MODE CONTROL
@app.route('/mode', methods=['POST'])
def set_mode():
    mode = request.json.get("mode")

    if mode in ["manual", "auto"]:
        system_state["mode"] = mode
        system_state["cycle_start"] = time.time()
        return jsonify({"status": f"{mode} mode activated"})

    return jsonify({"error": "Invalid mode"}), 400

# DMM CONTROL
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

# POWER SUPPLY CONTROL
@app.route('/psu/start', methods=['POST'])
def start_psu():

    global psu, psu_busy

    if not psu:
        return jsonify({"error":"PSU not connected"}),500

    try:
        psu_busy = True

        data = request.json or {}

        voltage = float(data.get("voltage",0))
        current = float(data.get("current",0))

        with psu_lock:

            psu.write(f"VSET1:{voltage:.3f}")
            time.sleep(0.2)

            psu.write(f"ISET1:{current:.3f}")
            time.sleep(0.2)

            psu.write("OUT1")
            time.sleep(0.5)

        system_state["psu_output"] = True
        system_state["psu_voltage"] = voltage
        system_state["psu_current"] = current

        return jsonify({"status":"started"})

    except Exception as e:

        return jsonify({"error":str(e)}),500

    finally:

        psu_busy = False

@app.route('/psu/stop', methods=['POST'])
def stop_psu():

    global psu, psu_busy

    if not psu:
        return jsonify({
            "error": "PSU not connected"
        }), 500

    try:

        psu_busy = True

        with psu_lock:

            psu.write("OUT0")
            time.sleep(0.5)

        system_state["psu_output"] = False
        system_state["psu_voltage"] = 0.0
        system_state["psu_current"] = 0.0

        return jsonify({
            "status": "stopped"
        })

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500

    finally:

        psu_busy = False

# NEW ROUTE
@app.route('/psu/set', methods=['POST'])
def set_psu():

    global psu, psu_busy

    if not psu:
        return jsonify({
            "error": "PSU not connected"
        }), 500

    data = request.json or {}

    voltage = float(data.get("voltage", 0))
    current = float(data.get("current", 0))

    try:

        psu_busy = True

        with psu_lock:

            psu.write(f"VSET1:{voltage:.3f}")
            time.sleep(0.2)

            psu.write(f"ISET1:{current:.3f}")
            time.sleep(0.2)

            #psu.write("OUT1")
            #time.sleep(0.1)

        system_state["psu_voltage"] = voltage
        system_state["psu_current"] = current

        return jsonify({
            "status": "updated"
        })

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500
    
    finally:
        psu_busy = False

# SAVE AUTO MODE CONFIGURATION
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

# DOWNLOAD CSV
@app.route('/download')
def download():
    return send_file(CSV_FILE, as_attachment=True)

# GET INSTRUMENT IDS
@app.route('/id')
def get_ids():
    return jsonify({
        "psu_id": psu.idn() if psu else "Not Connected",
        "dmm_id": dmm.idn() if dmm else "Not Connected"
    })

@app.route('/psu_raw')
def psu_raw():

    global psu

    if not psu:
        return "No PSU"

    cmds = [
        "VSET1?",
        "ISET1?",
        "STATUS?"
    ]

    for cmd in cmds:
        print(cmd, "=", psu.query(cmd))

    return "Done"

# GET AVAILABLE COM PORTS
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

# CONNECT DMM
@app.route('/connect_dmm', methods=['POST'])
def connect_dmm():

    global dmm

    data = request.json

    com_port = data.get("port")

    BAUDRATES = [9600, 19200, 38400, 57600, 115200]

    # CLOSE OLD CONNECTION FIRST
    try:
        if dmm:
            dmm.close()
            dmm = None
    except:
        pass

    # TRY DIFFERENT BAUDRATES
    for baud in BAUDRATES:

        test_dmm = None

        try:

            print(f"\nTrying baudrate: {baud}")

            test_dmm = Multimeter(
                port=com_port,
                baudrate=baud,
            #   timeout=2
            )

            # give instrument time
            time.sleep(1)

            response = test_dmm.idn()

            print("RAW ID RESPONSE:", response)

            # VALID RESPONSE CHECK
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

    # IF ALL BAUDRATES FAIL
    dmm = None

    return jsonify({
        "status": "error",
        "message": "Could not connect to DMM"
    }), 500

# MAIN
if __name__ == '__main__':
    app.run(
    debug=False,
    threaded=True
)
