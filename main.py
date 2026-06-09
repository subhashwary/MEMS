if system_state["psu_output"]:

    v = psu.query("VOUT1?")
    i = psu.query("IOUT1?")

else:

    v = "0"
    i = "0"
