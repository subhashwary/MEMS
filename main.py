def log_data(
    pressure,
    dmm_voltage,
    psu_voltage,
    psu_current,
    mode,
    ess_state,
    cycle,
    event
):
    with open(CSV_FILE, "a", newline="") as f:

        writer = csv.writer(f)

        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            pressure,
            dmm_voltage,
            psu_voltage,
            psu_current,
            mode,
            ess_state,
            cycle,
            event
        ])
