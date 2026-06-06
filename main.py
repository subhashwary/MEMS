@app.route('/psu/set', methods=['POST'])
def set_psu():

    data = request.json or {}

    voltage = float(data.get("voltage", 0))
    current = float(data.get("current", 0))

    # 🔴 PUT IT HERE (VERY TOP OF FUNCTION)
    if not psu:
        return jsonify({"error": "PSU not connected"}), 500

    try:
        with psu_lock:
            psu.write(f"VSET1:{voltage:.3f}\n")
            psu.write(f"ISET1:{current:.3f}\n")
            psu.write("OUT1\n")

        return jsonify({"status": "updated"})

    except Exception as e:
        return jsonify({"error": str(e)}), 500
