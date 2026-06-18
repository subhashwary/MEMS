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
                "Pressure",
                "DMM_Voltage",
                "PSU_Voltage",
                "PSU_Current",
                "Mode",
                "ESS_State",
                "Cycle",
                "Event"
            ])

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
