@app.route('/psu/start', methods=['POST'])
def start_psu():

    global psu, psu_busy

    if not psu:
        return jsonify({
            "error": "PSU not connected"
        }), 500

    data = request.json or {}

    voltage = float(data.get("voltage", 0))
    current = float(data.get("current", 0))

    try:

        psu_busy = True

        with psu_lock:

            psu.write(f"VSET1:{voltage:.3f}")
            psu.write(f"ISET1:{current:.3f}")
            psu.write("OUT1")

            system_state["psu_voltage"] = voltage
            system_state["psu_current"] = current

            time.sleep(1)

        return jsonify({
            "status": "started"
        })

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500

    finally:

        psu_busy = False
