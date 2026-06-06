try:

    candidate.write("VSET1:2.00")
    time.sleep(0.5)

    candidate.write("ISET1:0.10")
    time.sleep(0.5)

    psu = candidate

    return jsonify({
        "status": "connected",
        "baudrate": baud,
        "id": f"PSU Connected @ {baud}"
    })

except Exception:

    candidate.close()
