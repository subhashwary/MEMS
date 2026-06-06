try:

    candidate.write("VSET1:2.00")
    time.sleep(0.5)

    candidate.write("ISET1:0.10")
    time.sleep(0.5)

    psu = candidate

    print("\n================================")
    print("PSU CONNECTED SUCCESSFULLY")
    print("PORT:", com_port)
    print("BAUDRATE:", baud)
    print("================================\n")

    return jsonify({
        "status": "connected",
        "baudrate": baud,
        "id": f"PSU Connected @ {baud}"
    })

except Exception as e:

    print("PSU TEST FAILED:", e)

    candidate.close()
