@app.route('/data')
def data():

    # Simulated pressure reading
    system_state["pressure"] = round(random.uniform(20, 100), 2)

    if psu:
        time.sleep(0.2)

    # -----------------------------------------------------
    # AUTO MODE LOGIC
    # -----------------------------------------------------
    if system_state["mode"] == "auto":
        cfg = system_state["config"]
        elapsed = time.time() - system_state["cycle_start"]

        cycle_period = cfg["on_time"] + cfg["off_time"]

        if elapsed < cfg["initial_off"]:
            system_state["dmm_running"] = False
        else:
            adjusted = elapsed - cfg["initial_off"]
            position = adjusted % cycle_period
            system_state["dmm_running"] = position < cfg["on_time"]

    # -----------------------------------------------------
    # DMM READING
    # -----------------------------------------------------
    if system_state["dmm_running"]:
        if dmm:
            try:
                reading = dmm.measure_voltage()
                if isinstance(reading, (int, float)):
                    system_state["dmm_voltage"] = reading
            except Exception as e:
                print("DMM read error:", e)
                system_state["dmm_voltage"] = 0.0
        else:
            system_state["dmm_voltage"] = round(random.uniform(0, 10), 3)
    else:
        system_state["dmm_voltage"] = 0.0

    # -----------------------------------------------------
    # PSU READINGS (FIXED LOCATION)
    # -----------------------------------------------------
    PSU_READ_INTERVAL = 0.3

    last_psu_read = system_state.get("last_psu_read", 0)

    if psu and (time.time() - last_psu_read > PSU_READ_INTERVAL):

        try:
            with psu_lock:
                v = psu.query("VOUT1?")
                i = psu.query("IOUT1?")

            system_state["psu_voltage"] = parse_value(v)
            system_state["psu_current"] = parse_value(i)

            system_state["last_psu_read"] = time.time()

        except Exception as e:
            print("PSU read error:", e)

    # -----------------------------------------------------
    # LOG DATA
    # -----------------------------------------------------
    log_data(
        system_state["pressure"],
        system_state["dmm_voltage"],
        system_state["psu_voltage"],
        system_state["psu_current"],
        system_state["mode"]
    )

    return jsonify(system_state)
