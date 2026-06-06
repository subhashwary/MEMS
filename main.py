@app.route('/psu/set', methods=['POST'])
def set_psu():

    data = request.json or {}

    try:
        voltage = float(data.get("voltage", 0))
        current = float(data.get("current", 0))

        result = send_psu(voltage, current)

        if result != "OK":
            return jsonify({"error": result}), 500

        return jsonify({
            "status": "updated",
            "voltage": voltage,
            "current": current
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500
