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

@app.route('/data')
def data():
    # Simulated pressure reading (replace with real sensor data)
    system_state["pressure"] = round(random.uniform(20, 100), 2)

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
      
    if psu:
        try:

            with psu_lock:
                v = psu.get_voltage()
                i = psu.get_current()

            if v not in ["", "ERROR", None]:
                system_state["psu_voltage"] = float(v)

            if i not in ["", "ERROR", None]:
                system_state["psu_current"] = float(i)

        except Exception as e:

            print("PSU read error:", e)

    log_data(
        system_state["pressure"],
        system_state["dmm_voltage"],
        system_state["psu_voltage"],
        system_state["psu_current"],
        system_state["mode"]
    )

    return jsonify(system_state)

@app.route('/mode', methods=['POST'])
def set_mode():
    mode = request.json.get("mode")

    if mode in ["manual", "auto"]:
        system_state["mode"] = mode
        system_state["cycle_start"] = time.time()
        return jsonify({"status": f"{mode} mode activated"})

    return jsonify({"error": "Invalid mode"}), 400

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

@app.route('/psu/start', methods=['POST'])
def start_psu():

    global psu

    data = request.json or {}

    voltage = float(data.get("voltage", 0))
    current = float(data.get("current", 0))

    try:
        with psu_lock:
            psu.set_voltage(voltage)
            psu.set_current(current)

            psu.output_on()

        print("PSU OUTPUT ON")

        return jsonify({
            "status": "started"
        })

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500

@app.route('/psu/stop', methods=['POST'])
def stop_psu():

    try:

        psu.output_off()

        print("PSU OUTPUT OFF")

        return jsonify({
            "status":"stopped"
        })

    except Exception as e:

        return jsonify({
            "error":str(e)
        }), 500

@app.route('/psu/set', methods=['POST'])
def set_psu():

    global psu

    if not psu:
        return jsonify({
            "error": "PSU not connected"
        }), 500

    data = request.json

    voltage = float(data["voltage"])
    current = float(data["current"])

    try:

        print("\n====================")
        print("USER UPDATED PSU")
        print("Voltage =", voltage)
        print("Current =", current)
        print("====================")

        with psu_lock:
            psu.set_voltage(voltage)
            psu.set_current(current)

        # verify values
        try:
            print("VSET1? =", psu.query("VSET1?"))
            print("ISET1? =", psu.query("ISET1?"))
        except:
            pass

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
