@app.route('/psu_test')
def psu_test():

    global psu

    try:
        psu.write("VSET1:1.00")
        time.sleep(1)

        psu.write("ISET1:0.10")
        time.sleep(1)

        psu.write("OUT1")

        return "Commands Sent"

    except Exception as e:
        return str(e)
