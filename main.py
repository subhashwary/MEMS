with psu_lock:

    psu.ser.reset_input_buffer()

    v = psu.query("VOUT1?")
    i = psu.query("IOUT1?")

if not v or not i:

    print("WARNING: PSU returned empty response")

else:

    system_state["psu_voltage"] = parse_value(v)
    system_state["psu_current"] = parse_value(i)

    system_state["last_psu_read"] = time.time()
