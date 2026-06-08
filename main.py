try:

    global psu_busy

    psu_busy = True

    with psu_lock:

        psu.write(f"VSET1:{voltage:.3f}")
        psu.write(f"ISET1:{current:.3f}")
        psu.write("OUT1")

        system_state["psu_voltage"] = voltage
        system_state["psu_current"] = current

        psu.output_on()

        time.sleep(1.5)

        print("VERIFY VOUT =", psu.query("VOUT1?"))
        print("VERIFY IOUT =", psu.query("IOUT1?"))

    print("PSU OUTPUT ON")

    return jsonify({
        "status": "started"
    })

finally:

    psu_busy = False
