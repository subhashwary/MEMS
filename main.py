def initialize_csv():

    with open(CSV_FILE, "w", newline="") as f:

        writer = csv.writer(f)

        writer.writerow([
            "Timestamp",
            "DMM_Voltage",
            "PSU_Voltage",
            "Mode",
            "ESS_State",
            "Cycle",
            "Event"
        ])
