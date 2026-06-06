with psu_lock:
    v = psu.query("VOUT1?")
    i = psu.query("IOUT1?")
