@app.route('/mode', methods=['POST'])
def set_mode():

    mode = request.json.get("mode")

    print("MODE REQUEST =", mode)
