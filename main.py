@app.route('/psu_debug')
def psu_debug():

    global psu

    if not psu:
        return "No PSU"

    try:

        print("VSET1? =", psu.query("VSET1?"))
        print("ISET1? =", psu.query("ISET1?"))
        print("VOUT1? =", psu.query("VOUT1?"))
        print("IOUT1? =", psu.query("IOUT1?"))

        return "Done"

    except Exception as e:
        return str(e)
