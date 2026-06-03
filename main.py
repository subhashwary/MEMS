@app.route('/psu/set', methods=['POST'])
def set_psu():

    global psu

    data = request.json

    voltage = float(data["voltage"])
    current = float(data["current"])

    try:

        psu.set_voltage(voltage)
        psu.set_current(current)

        return jsonify({
            "status": "Settings Updated"
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500
