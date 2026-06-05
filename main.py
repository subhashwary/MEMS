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

        print("\n====================")
        print("USER UPDATED PSU")
        print("Voltage =", voltage)
        print("Current =", current)
        print("====================")

        psu.set_voltage(voltage)
        psu.set_current(current)

        return jsonify({
            "status": "updated",
            "voltage": voltage,
            "current": current
        })

    except Exception as e:

        print("PSU ERROR:", e)

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
