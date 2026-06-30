def ess_loop():

    while True:

        update_ess_state()

        read_psu()

        read_dmm()

        log_csv()

        time.sleep(0.1)
