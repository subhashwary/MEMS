return jsonify({
    "psu_connected": psu is not None,
    "dmm_connected": dmm is not None,
    "psu_output": system_state["psu_output"],
    "voltage": system_state["psu_voltage"],
    "current": system_state["psu_current"]
})
