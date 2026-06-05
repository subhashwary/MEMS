@app.route('/psu/set', methods=['POST'])
def set_psu():

    data = request.json

    voltage = float(data["voltage"])
    current = float(data["current"])

    print()
    print("===============")
    print("USER SET PSU")
    print("Voltage:", voltage)
    print("Current:", current)
    print("===============")

    psu.set_voltage(voltage)
    psu.set_current(current)

    return jsonify({
        "status": "ok"
    })
