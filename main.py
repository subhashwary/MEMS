@app.route('/mode', methods=['POST'])
def set_mode():

    mode = request.json.get("mode")

    if mode == "manual":

        system_state["mode"] = "manual"
        system_state["auto_running"] = False

        return jsonify({"status":"manual mode"})

    elif mode == "auto":

        system_state["mode"] = "auto"
        system_state["auto_running"] = True
        system_state["cycle_start"] = time.time()

        return jsonify({"status":"auto mode"})

    return jsonify({"error":"Invalid mode"}),400
