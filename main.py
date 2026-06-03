@app.route('/psu/start', methods=['POST'])
def start_psu():

    global psu

    data = request.json or {}

    voltage = float(data.get("voltage", 0))
    current = float(data.get("current", 0))

    if not psu:
        return jsonify({"error": "PSU not connected"}), 500

    try:

        psu.set_voltage(voltage)
        psu.set_current(current)

        psu.output_on()

        system_state["dmm_running"] = True

        return jsonify({
            "status": "PSU started",
            "voltage": voltage,
            "current": current
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500
