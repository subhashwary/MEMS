try:

    print(f"Setting Voltage = {voltage}")
    print(f"Setting Current = {current}")

    psu.set_voltage(voltage)
    psu.set_current(current)

    # Verify PSU accepted values
    print("VERIFY VSET =", psu.query("VSET1?"))
    print("VERIFY ISET =", psu.query("ISET1?"))

    psu.output_on()

    print("PSU OUTPUT ON")

    return jsonify({
        "status": "PSU started",
        "voltage": voltage,
        "current": current
    })

except Exception as e:

    print("PSU START ERROR:", e)

    return jsonify({"error": str(e)}), 500
