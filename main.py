@app.route('/psu_test')
def psu_test():

    global psu

    if not psu:
        return jsonify({"error": "PSU not connected"})

    try:

        with psu_lock:

            print("SETTING VOLTAGE...")
            psu.write("VSET1:2.00")
            time.sleep(1)

            print("SETTING CURRENT...")
            psu.write("ISET1:0.10")
            time.sleep(1)

            print("OUTPUT ON...")
            psu.write("OUT1")
            time.sleep(1)

            vset = psu.query("VSET1?")
            iset = psu.query("ISET1?")

            try:
                vout = psu.query("VOUT1?")
            except:
                vout = "N/A"

            try:
                iout = psu.query("IOUT1?")
            except:
                iout = "N/A"

            result = {
                "VSET1": vset,
                "ISET1": iset,
                "VOUT1": vout,
                "IOUT1": iout
            }

            print(result)

            return jsonify(result)

    except Exception as e:

        return jsonify({
            "error": str(e)
        })
