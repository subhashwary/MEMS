@app.route("/data")
def data():

    return jsonify({

        **system_state,

        "mode_numeric":
            1 if system_state["mode"] == "auto" else 0,

        "ess_numeric":
            2 if "ON" in system_state["ess_state"]
            else 1 if system_state["ess_state"] == "INITIAL_DELAY"
            else 0

    })
