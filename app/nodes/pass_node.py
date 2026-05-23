def pass_node(state):

    print("\n=== PASS NODE ===")

    state["messages"].append(
        "Checkpoint passed!"
    )

    state["completed"] = True

    return state