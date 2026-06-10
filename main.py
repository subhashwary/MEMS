return jsonify({

    "psu_connected": psu is not None,

    "dmm_connected": dmm is not None,

    "psu_output": system_state["psu_output"],

    "auto_running": system_state["auto_running"],

    "ess_state": system_state["ess_state"],

    "voltage": system_state["psu_voltage"],

    "current": system_state["psu_current"]

})
