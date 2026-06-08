global psu_busy

with psu_lock:

    psu_busy = True




psu_busy = False
