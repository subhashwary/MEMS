@app.route('/status')
def status():

    return jsonify({
        "psu_connected": psu is not None,
        "dmm_connected": dmm is not None
    })
