v = psu.query("VOUT1?")
i = psu.query("IOUT1?")

system_state["psu_voltage"] = parse_value(v)
system_state["psu_current"] = parse_value(i)
