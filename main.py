if (
    system_state["mode"] == "auto"
    and system_state["auto_running"]
):

    cfg = system_state["config"]

    elapsed = time.time() - system_state["cycle_start"]

    initial_delay = cfg["initial_off"]
    on_time = cfg["on_time"]
    off_time = cfg["off_time"]
    cycles = cfg["cycles"]

    cycle_period = on_time + off_time
