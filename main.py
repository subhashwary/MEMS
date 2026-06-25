@app.route('/reset', methods=['POST'])
def reset():

    global system_state

    system_state["mode"] = "manual"
    system_state["auto_running"] = False
    system_state["dmm_running"] = False

    system_state["current_cycle"] = 0
    system_state["cycle_event"] = "Waiting"
    system_state["ess_state"] = "IDLE"

    system_state["dmm_voltage"] = 0.0
    system_state["psu_voltage"] = 0.0
    system_state["psu_current"] = 0.0
    system_state["pressure"] = 0.0

    system_state["cycle_start"] = time.time()

    # Erase old CSV and create fresh one
    initialize_csv()

    return jsonify({
        "status": "reset complete"
    })
