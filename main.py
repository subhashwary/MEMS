try:

    with psu_lock:

        if psu:
            psu.close()

        psu = PowerSupply(
            port=com_port,
            baudrate=9600,
            timeout=2
        )

        response = psu.idn()

except Exception as e:

    psu = None

    return jsonify({
        "status": "error",
        "message": str(e)
    }), 500
