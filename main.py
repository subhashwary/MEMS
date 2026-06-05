@app.route('/psu/set', methods=['POST'])
def set_psu():

    global psu

    if not psu:
        return jsonify({
            "error": "PSU not connected"
        }), 500

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

        # verify values
        try:
            print("VSET1? =", psu.query("VSET1?"))
            print("ISET1? =", psu.query("ISET1?"))
        except:
            pass

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
