def send_psu(voltage, current):
    global psu

    if not psu:
        return "PSU not connected"

    try:
        with psu_lock:

            cmd_v = f"VSET1:{voltage:.3f}"
            cmd_i = f"ISET1:{current:.3f}"

            psu.write(cmd_v)
            time.sleep(0.05)
            psu.write(cmd_i)
            time.sleep(0.05)

            # optional verification (safe)
            try:
                v = psu.query("VSET1?")
                i = psu.query("ISET1?")
                print("VERIFIED:", v, i)
            except:
                pass

        return "OK"

    except Exception as e:
        return str(e)
