if system_state["mode"] == "auto":
    return jsonify({
        "error": "PSU settings locked in AUTO mode"
    }), 403
