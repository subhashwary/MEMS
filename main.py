with psu_lock:

    psu.write(f"VSET1:{voltage:.3f}")
    psu.write(f"ISET1:{current:.3f}")
    psu.write("OUT1")

system_state["psu_voltage"] = voltage
system_state["psu_current"] = current

return jsonify({"status": "updated"})
