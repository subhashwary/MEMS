"ess_numeric":
    2 if "ON" in system_state["ess_state"]
    else 1 if system_state["ess_state"] == "INITIAL_DELAY"
    else 0
