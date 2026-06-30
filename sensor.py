@app.route('/config', methods=['POST'])
def save_config():

    data = request.json or {}

    voltage = float(data.get("voltage", 2.0))
    current = float(data.get("current", 0.1))

    initial_off = max(1, int(data.get("initial_off", 5)))
    on_time = max(1, int(data.get("on_time", 5)))
    off_time = max(1, int(data.get("off_time", 5)))
    cycles = max(1, int(data.get("cycles", 10)))

    system_state["config"] = {

        "voltage": voltage,
        "current": current,

        "initial_off": initial_off,
        "on_time": on_time,
        "off_time": off_time,
        "cycles": cycles
    }

    system_state["cycle_start"] = time.time()

    return jsonify({
        "status": "Configuration Saved",
        "config": system_state["config"]
    })
