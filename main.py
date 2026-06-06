system_state = {
    "mode": "manual",
    "dmm_running": False,
    "dmm_voltage": 0.0,
    "pressure": 0.0,
    "psu_voltage": 0.0,
    "psu_current": 0.0,
    "cycle_start": time.time(),

    # 🔴 ADD THIS LINE
    "last_psu_read": 0,

    "config": {
        "initial_off": 5,
        "on_time": 5,
        "off_time": 5,
        "cycles": 10
    }
}
