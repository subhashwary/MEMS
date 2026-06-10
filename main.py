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

    if elapsed < initial_delay:

        system_state["ess_state"] = "INITIAL_DELAY"

        system_state["current_cycle"] = 0

        system_state["dmm_running"] = False

        if system_state["psu_output"]:

            try:
                with psu_lock:
                    psu.write("OUT0")
            except:
                pass

            system_state["psu_output"] = False

    else:

        adjusted = elapsed - initial_delay

        completed_cycles = int(
            adjusted // cycle_period
        )

