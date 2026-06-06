if not psu:
    return jsonify({"error": "PSU not connected"}), 500
