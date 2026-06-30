if system_state["dmm_running"]:

            if dmm:

                try:

                    reading = dmm.measure_voltage()

                    if isinstance(reading, (int, float)):

                        system_state["dmm_voltage"] = reading

                except Exception as e:

                    print(e)

                    system_state["dmm_voltage"] = 0.0

            else:

                system_state["dmm_voltage"] = round(
                    random.uniform(0, 10),
                    3
                )

        else:

            system_state["dmm_voltage"] = 0.0
