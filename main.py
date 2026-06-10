@app.route('/auto/start', methods=['POST'])
def auto_start():

    system_state["mode"] = "auto"

    system_state["cycle_start"] = time.time()

    system_state["auto_running"] = True

    system_state["current_cycle"] = 0

    system_state["ess_state"] = "INITIAL_DELAY"

    return jsonify({
        "status":"started"
    })


@app.route('/auto/stop', methods=['POST'])
def auto_stop():

    global psu

    system_state["auto_running"] = False

    system_state["ess_state"] = "STOPPED"

    system_state["dmm_running"] = False

    if psu:

        try:
            with psu_lock:
                psu.write("OUT0")
        except:
            pass

    system_state["psu_output"] = False

    return jsonify({
        "status":"stopped"
    })
