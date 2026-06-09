# POWER SUPPLY CONTROL
@app.route('/psu/start', methods=['POST'])
def start_psu():

    global psu, psu_busy

    if not psu:
        return jsonify({"error":"PSU not connected"}),500

    try:

        data = request.json or {}

        voltage = float(data.get("voltage",0))
        current = float(data.get("current",0))

        with psu_lock:

            psu.write(f"VSET1:{voltage:.3f}")
            time.sleep(0.2)

            psu.write(f"ISET1:{current:.3f}")
            time.sleep(0.2)

            psu.write("OUT1")
            time.sleep(0.5)

        system_state["psu_output"] = True

        return jsonify({"status":"started"})

    except Exception as e:

        return jsonify({"error":str(e)}),500

    finally:

        psu_busy = False

@app.route('/psu/stop', methods=['POST'])
def stop_psu():

    global psu, psu_busy

    if not psu:
        return jsonify({"error":"PSU not connected"}),500

    try:

        psu_busy = True

        with psu_lock:

            psu.write("OUT0")
            time.sleep(0.5)

    finally:
        psu_busy = False

        system_state["psu_output"] = False

        return jsonify({"status":"stopped"})

    except Exception as e:

        return jsonify({"error":str(e)}),500

