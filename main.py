@app.route('/psu_raw')
def psu_raw():

    global psu

    if not psu:
        return "No PSU"

    cmds = [
        "VSET1?",
        "ISET1?",
        "STATUS?"
    ]

    for cmd in cmds:
        print(cmd, "=", psu.query(cmd))

    return "Done"
