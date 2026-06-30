def background_worker():

    global psu

    while True:

        # -------------------------------------------------
        # 1. TIMESTAMP
        # -------------------------------------------------

        system_state["timestamp"] = (
            datetime.now().strftime("%H:%M:%S.%f")[:-3]
        )


        # -------------------------------------------------
        # 2. ESS UPDATE
        # -------------------------------------------------


        # ESS code goes here



        # -------------------------------------------------
        # 3. PSU READ
        # -------------------------------------------------


        # PSU read code goes here



        # -------------------------------------------------
        # 4. DMM READ
        # -------------------------------------------------


        # DMM read code goes here



        # -------------------------------------------------
        # 5. CSV LOG
        # -------------------------------------------------

        log_data(
            system_state["dmm_voltage"],
            system_state["psu_voltage"],
            system_state["mode"],
            system_state["ess_state"],
            system_state["current_cycle"],
            system_state["cycle_event"]
        )


        # -------------------------------------------------
        # 6. LOOP DELAY
        # -------------------------------------------------

        time.sleep(0.1)
