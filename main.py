if position < on_time:

    system_state["ess_state"] = f"CYCLE_{cycle_no}_ON"
    system_state["cycle_event"] = f"Cycle {cycle_no} ON"
    system_state["dmm_running"] = True

    if psu and not system_state["psu_output"]:
        psu.write("OUT1")
        system_state["psu_output"] = True

else:

    system_state["ess_state"] = f"CYCLE_{cycle_no}_OFF"
    system_state["cycle_event"] = f"Cycle {cycle_no} OFF"
    system_state["dmm_running"] = False

    if psu and system_state["psu_output"]:
        psu.write("OUT0")
        system_state["psu_output"] = False
