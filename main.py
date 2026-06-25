import csv
import os
from datetime import datetime

CSV_FILE = "sensor_data.csv"

def initialize_csv():
    if not os.path.exists(CSV_FILE):
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

def log_data(
    dmm_voltage,
    psu_voltage,
    mode,
    ess_state,
    cycle,
    event
):
    with open(CSV_FILE, "a", newline="") as f:

        writer = csv.writer(f)

        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            dmm_voltage,
            psu_voltage,
            mode,
            ess_state,
            cycle,
            event
        ])
