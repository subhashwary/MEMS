@app.route('/mode', methods=['POST'])
def set_mode():

    mode = request.json.get("mode")

    print("MODE REQUEST =", mode)

    if mode == "manual":

        system_state["mode"] = "manual"
        system_state["auto_running"] = False

        return jsonify({"status":"manual mode"})

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

        return jsonify({
            "status": "auto mode"
        })

    return jsonify({"error":"Invalid mode"}),400
