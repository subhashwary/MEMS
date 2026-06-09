@app.route('/psu_debug')
def psu_debug():

    global psu

    if not psu:
        return jsonify({"error": "No PSU"})

    try:

        result = {
            "VSET1": psu.query("VSET1?"),
            "ISET1": psu.query("ISET1?"),
            "VOUT1": psu.query("VOUT1?"),
            "IOUT1": psu.query("IOUT1?")
        }

        print(result)

        return jsonify(result)

    except Exception as e:

        return jsonify({
            "error": str(e)
        })
