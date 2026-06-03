@app.route('/psu/set', methods=['POST'])
def set_psu():

    global psu

    data = request.json or {}

    voltage = float(data.get("voltage", 5))
    current = float(data.get("current", 0.1))

    if not psu:
        return jsonify({"error": "PSU not connected"}), 500

    try:
        psu.set_voltage(voltage)
        psu.set_current(current)

        return jsonify({
            "status": "Values Set",
            "voltage": voltage,
            "current": current
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500
