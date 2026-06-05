@app.route('/psu/set', methods=['POST'])
def set_psu():

    global psu

    data = request.json

    voltage = float(data["voltage"])
    current = float(data["current"])

    try:

        print("\n====================")
        print("USER UPDATED PSU")
        print("Voltage =", voltage)
        print("Current =", current)
        print("====================")

        psu.set_voltage(voltage)
        psu.set_current(current)

        return jsonify({
            "status": "updated",
            "voltage": voltage,
            "current": current
        })

    except Exception as e:

        print("PSU ERROR:", e)

        return jsonify({
            "error": str(e)
        }), 500
