initial_off = max(1, int(data.get("initial_off", 5)))
on_time = max(1, int(data.get("on_time", 5)))
off_time = max(1, int(data.get("off_time", 5)))
cycles = max(1, int(data.get("cycles", 10)))

system_state["config"] = {
    "initial_off": initial_off,
    "on_time": on_time,
    "off_time": off_time,
    "cycles": cycles
}
