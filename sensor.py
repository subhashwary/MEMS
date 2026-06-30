timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]

def background_worker():

    while True:

        system_state["timestamp"] = (
            datetime.now()
            .strftime("%H:%M:%S.%f")[:-3]
        )

        # ESS Logic

        # PSU Read

        # DMM Read

        # CSV Logging

        time.sleep(0.1)
