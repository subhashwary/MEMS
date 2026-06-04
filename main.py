@app.route('/connect_psu', methods=['POST'])
def connect_psu():

    global psu

    data = request.json

    com_port = data.get("port")

    try:

        if psu:
            psu.close()

    except:
        pass

    try:

        psu = PowerSupply(
            port=com_port,
            baudrate=9600,
            timeout=2
        )

        response = psu.idn()

        print("\n========================")
        print("PSU CONNECTED")
        print("PORT:", com_port)
        print("ID:", response)
        print("========================\n")

        return jsonify({
            "status": "connected",
            "id": response
        })

    except Exception as e:

        psu = None

        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500
