if (
    psu
    and not psu_busy
    and (time.time() - last_psu_read > PSU_READ_INTERVAL)
):

    try:

        with psu_lock:

            psu.ser.reset_input_buffer()

            v = psu.query("VOUT1?")
            i = psu.query("IOUT1?")
