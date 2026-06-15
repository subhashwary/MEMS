return jsonify({

    **system_state,

    "timestamp": time.strftime("%H:%M:%S"),

    "mode_numeric":
        1 if system_state["mode"] == "auto" else 0,

    "ess_numeric":
        1 if system_state["psu_output"] else 0
})
