# DOWNLOAD CSV
@app.route('/download')
def download():
    return send_file(CSV_FILE, as_attachment=True)


# RESET SYSTEM
@app.route('/reset', methods=['POST'])
def reset():

    global system_state

    system_state["current_cycle"] = 0
    system_state["auto_running"] = False
    system_state["cycle_event"] = "Waiting"
    system_state["ess_state"] = "IDLE"
    system_state["dmm_voltage"] = 0.0
    system_state["psu_voltage"] = 0.0
    system_state["psu_current"] = 0.0
    system_state["pressure"] = 0.0

    # Create fresh CSV
    initialize_csv()

    return jsonify({
        "status": "reset complete"
    })


# MAIN
if __name__ == '__main__':
    app.run(
        debug=False,
        threaded=True
    )
