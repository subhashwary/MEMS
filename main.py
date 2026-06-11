if completed_cycles >= cycles:

    system_state["auto_running"] = False
    system_state["mode"] = "manual"

    system_state["ess_state"] = "COMPLETE"
    system_state["cycle_event"] = "ESS Completed"
