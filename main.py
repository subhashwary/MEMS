def send_psu(voltage, current):
    global psu

    if not psu:
        return "PSU not connected"

    try:
        with psu_lock:

            cmd_v = f"VSET1:{voltage:.3f}\r\n"
            cmd_i = f"ISET1:{current:.3f}\r\n"

            psu.write(cmd_v)
            time.sleep(0.1)

            psu.write(cmd_i)
            time.sleep(0.1)

            psu.write("OUT1\r\n")

        return "OK"

    except Exception as e:
        return str(e)
