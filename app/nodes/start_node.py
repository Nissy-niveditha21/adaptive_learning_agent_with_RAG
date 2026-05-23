def start_learning(state):

    print("\n=== START NODE ===")

    first_checkpoint = state["checkpoints"][0]

    state["current_checkpoint"] = first_checkpoint

    state["messages"].append(
        f"Starting topic: {state['topic']}"
    )

    state["messages"].append(
        f"Loaded checkpoint: {first_checkpoint['title']}"
    )

    return state