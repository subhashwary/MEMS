@app.route('/psu/stop', methods=['POST'])
def stop_psu():

    try:

        psu.output_off()

        print("PSU OUTPUT OFF")

        return jsonify({
            "status":"stopped"
        })

    except Exception as e:

        return jsonify({
            "error":str(e)
        }), 500
