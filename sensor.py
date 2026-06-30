@app.route('/mode', methods=['POST'])
def set_mode():

    global psu

    data = request.json or {}
    mode = data.get("mode")

    print("MODE REQUEST =", mode)

    if mode == "manual":

        system_state["mode"] = "manual"
        system_state["auto_running"] = False
        system_state["dmm_running"] = False

        if psu and system_state["psu_output"]:
            try:
                with psu_lock:
                    psu.write("OUT0")
                    time.sleep(0.2)
            except Exception as e:
                print("PSU OFF ERROR:", e)

        system_state["psu_output"] = False
        system_state["psu_voltage"] = 0.0
        system_state["psu_current"] = 0.0

        system_state["ess_state"] = "IDLE"
        system_state["cycle_event"] = "Waiting"
        system_state["current_cycle"] = 0

        return jsonify({
            "status": "manual mode"
        })


    elif mode == "auto":

        if not psu:
            return jsonify({
                "error": "Connect PSU first"
            }), 400

        if not dmm:
            return jsonify({
                "error": "Connect DMM first"
            }), 400

        system_state["mode"] = "auto"
        system_state["auto_running"] = True

        system_state["cycle_start"] = time.time()

        system_state["current_cycle"] = 0

        system_state["ess_state"] = "INITIAL_DELAY"
        system_state["cycle_event"] = "Starting ESS"

        system_state["dmm_running"] = False

        system_state["psu_output"] = False
        system_state["psu_voltage"] = 0.0
        system_state["psu_current"] = 0.0

        print("AUTO MODE STARTED")

        return jsonify({
            "status": "auto mode"
        })

    return jsonify({
        "error": "Invalid mode"
    }), 400
