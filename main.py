@app.route('/psu_test')
def psu_test():

    global psu

    try:

        print("Sending VSET1:2.00")
        psu.write("VSET1:2.00")

        time.sleep(1)

        print("Sending ISET1:0.10")
        psu.write("ISET1:0.10")

        time.sleep(1)

        print("Sending OUT1")
        psu.write("OUT1")

        return "Commands Sent"

    except Exception as e:

        return str(e)
