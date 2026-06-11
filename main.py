elif mode == "auto":

    system_state["mode"] = "auto"
    system_state["auto_running"] = True

    system_state["cycle_start"] = time.time()

    system_state["current_cycle"] = 0
    system_state["ess_state"] = "INITIAL_DELAY"
    system_state["cycle_event"] = "Starting ESS"

    return jsonify({
        "status":"auto mode"
    })
