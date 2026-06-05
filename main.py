@app.route('/psu/set', methods=['POST'])
def set_psu():

    global psu

    data = request.json

    voltage = float(data["voltage"])
    current = float(data["current"])

    try:

        psu.set_voltage(voltage)
        psu.set_current(current)

        print(f"SET V={voltage}")
        print(f"SET I={current}")

        return jsonify({
            "status": "updated"
        })

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500
