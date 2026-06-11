else:

    cycle_no = completed_cycles + 1

    position = adjusted % cycle_period

    print("cycle_no =", cycle_no)
    print("position =", position)

    system_state["current_cycle"] = cycle_no
