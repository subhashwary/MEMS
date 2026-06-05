@app.route('/connect_psu', methods=['POST'])
def connect_psu():

    global psu

    data = request.json
    com_port = data.get("port")

    with psu_lock:

        # Close previous PSU connection if any
        try:
            if psu:
                psu.close()
        except:
            pass

        try:

            psu = None
            response = ""

            # Try common baud rates
            for baud in [9600, 19200, 38400, 57600]:

                try:

                    print(f"\nTrying PSU baudrate: {baud}")

                    candidate = PowerSupply(
                        port=com_port,
                        baudrate=baud,
                        timeout=2
                    )

                    print("IDN  =", candidate.query("*IDN?"))
                    print("VSET =", candidate.query("VSET1?"))
                    print("ISET =", candidate.query("ISET1?"))

                    response = candidate.query("*IDN?")

                    # If we get any valid response, keep this connection
                    if response:

                        psu = candidate

                        print("\n================================")
                        print("PSU CONNECTED SUCCESSFULLY")
                        print("PORT:", com_port)
                        print("BAUDRATE:", baud)
                        print("ID:", response)
                        print("================================\n")

                        return jsonify({
                            "status": "connected",
                            "baudrate": baud,
                            "id": response
                        })

                    else:
                        candidate.close()

                except Exception as e:

                    print(f"Failed at {baud}: {e}")

            # If all baud rates fail
            psu = None

            return jsonify({
                "status": "error",
                "message": "No response from PSU on any baud rate"
            }), 500

        except Exception as e:

            psu = None

            return jsonify({
                "status": "error",
                "message": str(e)
            }), 500
