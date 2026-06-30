        if (
            system_state["mode"] == "auto"
            and system_state["auto_running"]
        ):
            
            print("AUTO LOOP RUNNING")

            cfg = system_state["config"]

            elapsed = time.time() - system_state["cycle_start"]

            initial_delay = cfg["initial_off"]
            on_time = cfg["on_time"]
            off_time = cfg["off_time"]
            cycles = cfg["cycles"]

            cycle_period = on_time + off_time

            # -------------------------
            # INITIAL DELAY
            # -------------------------

            if elapsed < initial_delay:

                system_state["ess_state"] = "INITIAL_DELAY"
                system_state["cycle_event"] = "Waiting Initial Delay"
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

                # -------------------------
                # ESS COMPLETE
                # -------------------------

                if completed_cycles >= cycles:

                    system_state["auto_running"] = False
                    system_state["mode"] = "manual"

                    system_state["ess_state"] = "COMPLETE"
                    system_state["cycle_event"] = "ESS Completed"

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

                    # -------------------------
                    # ON PERIOD
                    # -------------------------

                    if position < on_time:

                        system_state["ess_state"] = f"CYCLE_{cycle_no}_ON"

                        system_state["event_timestamp"] = (
                            datetime.now().strftime("%H:%M:%S.%f")[:-3]
                        )

                        system_state["event_name"] = (
                            f"Cycle {cycle_no} ON"
                        )

                        system_state["cycle_event"] = (
                            f"Cycle {cycle_no} ON"
                        )

                        system_state["dmm_running"] = True

                        if psu and not system_state["psu_output"]:

                            try:

                                voltage = system_state["config"]["voltage"]
                                current = system_state["config"]["current"]

                                with psu_lock:

                                    psu.write(f"VSET1:{voltage:.3f}")
                                    time.sleep(0.2)

                                    psu.write(f"ISET1:{current:.3f}")
                                    time.sleep(0.2)

                                    psu.write("OUT1")
                                    time.sleep(0.2)

                                system_state["psu_output"] = True
                                system_state["psu_voltage"] = voltage
                                system_state["psu_current"] = current

                                print(f"Cycle {cycle_no}: PSU ON")
                                print(f"Voltage = {voltage} V")
                                print(f"Current = {current} A")

                            except Exception as e:

                                print("PSU ON ERROR:", e)

                    else:

                        system_state["ess_state"] = f"CYCLE_{cycle_no}_OFF"

                        system_state["event_timestamp"] = (
                            datetime.now().strftime("%H:%M:%S.%f")[:-3]
                        )

                        system_state["event_name"] = (
                            f"Cycle {cycle_no} OFF"
                        )

                        system_state["cycle_event"] = (
                            f"Cycle {cycle_no} OFF"
                        )

                        system_state["dmm_running"] = False

                        if psu and system_state["psu_output"]:

                            try:

                                with psu_lock:
                                    psu.write("OUT0")
                                    time.sleep(0.2)

                                system_state["psu_output"] = False
                                system_state["psu_voltage"] = 0.0
                                system_state["psu_current"] = 0.0

                                print(f"Cycle {cycle_no} PSU OFF")

                            except Exception as e:

                                print("PSU OFF ERROR:", e)
