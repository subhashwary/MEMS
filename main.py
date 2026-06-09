if (
    psu
    and not psu_busy
    and (time.time() - last_psu_read > PSU_READ_INTERVAL)
):

    try:

        with psu_lock:

            v = psu.query("VSET1?")
            i = psu.query("ISET1?")

        print("PSU V =", v)
        print("PSU I =", i)

        if not v or not i:

            print("WARNING: PSU returned empty response")

        else:

            system_state["psu_voltage"] = parse_value(v)
            system_state["psu_current"] = parse_value(i)

            system_state["last_psu_read"] = time.time()

    except Exception as e:

        print("PSU read error:", e)
