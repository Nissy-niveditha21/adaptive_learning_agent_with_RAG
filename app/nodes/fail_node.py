def fail_node(state):

    print("\n=== FAIL NODE ===")

    state["messages"].append(
        "Checkpoint failed!"
    )

    state["completed"] = False

    return state