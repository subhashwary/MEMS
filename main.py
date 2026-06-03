@app.route('/psu/start', methods=['POST'])
def start_psu():

    global psu

    if not psu:
        return jsonify({"error": "PSU not connected"}), 500

    try:

        psu.output_on()

        system_state["dmm_running"] = True

        return jsonify({
            "status": "PSU started"
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500
