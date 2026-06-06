@app.route('/psu/set', methods=['POST'])
def set_psu():

    global psu

    if not psu:
        return jsonify({
            "error": "PSU not connected"
        }), 500

    data = request.json or {}

    voltage = float(data.get("voltage", 0))
    current = float(data.get("current", 0))

    try:

        with psu_lock:

            psu.write(f"VSET1:{voltage:.3f}")
            psu.write(f"ISET1:{current:.3f}")
            psu.write("OUT1")

        # Update UI immediately
        system_state["psu_voltage"] = voltage
        system_state["psu_current"] = current

        return jsonify({
            "status": "updated"
        })

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500
