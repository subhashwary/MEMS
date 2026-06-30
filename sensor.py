timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]


worker = Thread(
    target=background_worker,
    daemon=True
)

worker.start()

app.run(
    debug=False,
    threaded=True
)
