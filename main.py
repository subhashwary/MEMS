if system_state["mode"] == "auto":
    return jsonify({
        "error": "Manual PSU control disabled in AUTO mode"
    }), 403
