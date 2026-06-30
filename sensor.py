system_state["event_timestamp"] = (
    datetime.now().strftime("%H:%M:%S.%f")[:-3]
)

system_state["event_name"] = (
    f"Cycle {cycle_no} OFF"
)
