if elapsed < initial_delay:

    system_state["ess_state"] = "INITIAL_DELAY"
    system_state["cycle_event"] = "Waiting Initial Delay"
    system_state["current_cycle"] = 0
    system_state["dmm_running"] = False

    if psu and system_state["psu_output"]:
        try:
            with psu_lock:
                psu.write("OUT0")
        except:
            pass

        system_state["psu_output"] = False

else:

    adjusted = elapsed - initial_delay

    completed_cycles = int(adjusted // cycle_period)

    if completed_cycles >= cycles:

        system_state["auto_running"] = False

        system_state["ess_state"] = "COMPLETE"
        system_state["cycle_event"] = "ESS Completed"

        system_state["dmm_running"] = False

        if psu and system_state["psu_output"]:

            try:
                with psu_lock:
                    psu.write("OUT0")
            except:
                pass

            system_state["psu_output"] = False

    else:

        cycle_no = completed_cycles + 1

        position = adjusted % cycle_period

        system_state["current_cycle"] = cycle_no

        if position < on_time:

            system_state["ess_state"] = f"CYCLE_{cycle_no}_ON"
            system_state["cycle_event"] = f"Cycle {cycle_no} ON"

            system_state["dmm_running"] = True

            if psu and not system_state["psu_output"]:

                try:
                    with psu_lock:
                        psu.write("OUT1")

                    system_state["psu_output"] = True

                except Exception as e:
                    print("PSU ON ERROR:", e)

        else:

            system_state["ess_state"] = f"CYCLE_{cycle_no}_OFF"
            system_state["cycle_event"] = f"Cycle {cycle_no} OFF"

            system_state["dmm_running"] = False

            if psu and system_state["psu_output"]:

                try:
                    with psu_lock:
                        psu.write("OUT0")

                    system_state["psu_output"] = False

                except Exception as e:
                    print("PSU OFF ERROR:", e)
