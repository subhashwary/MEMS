@app.route('/psu/stop', methods=['POST'])
def stop_psu():

    global psu

    if not psu:
        return jsonify({"error":"PSU not connected"}),500

    try:

        with psu_lock:

            psu.write("OUT0")
            time.sleep(0.5)

        system_state["psu_output"] = False

        return jsonify({"status":"stopped"})

    except Exception as e:

        return jsonify({"error":str(e)}),500
