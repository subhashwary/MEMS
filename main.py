@app.route('/psu/set', methods=['POST'])
def set_psu():
    global psu

    if not psu:
        return jsonify({"error": "PSU not connected"}), 500

    data = request.json or {}

    voltage = float(data.get("voltage", 0))
    current = float(data.get("current", 0))

    try:
        with psu_lock:

            psu.write(f"VSET1:{voltage}")
            psu.write(f"ISET1:{current}")

            time.sleep(0.2)

            v = psu.query("VSET1?")
            i = psu.query("ISET1?")

        return jsonify({
            "status": "updated",
            "voltage": parse_value(v),
            "current": parse_value(i)
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500
