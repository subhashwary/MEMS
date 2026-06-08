with psu_lock:

    psu.write(f"VSET1:{voltage:.3f}")
    time.sleep(0.1)

    psu.write(f"ISET1:{current:.3f}")
    time.sleep(0.1)

    psu.write("OUT1")
    time.sleep(0.1)
