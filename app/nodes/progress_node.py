def progress_node(state):

    print("\n=== PROGRESS NODE ===")

    current_checkpoint = state["current_checkpoint"]

    state["completed_checkpoints"].append(
        current_checkpoint["id"]
    )

    current_index = state["current_checkpoint_index"]

    next_index = current_index + 1

    if next_index >= len(state["checkpoints"]):

        state["session_complete"] = True

        state["messages"].append(
            "All checkpoints completed!"
        )

        print("\nLearning session completed.")

    else:

        state["current_checkpoint_index"] = next_index

        next_checkpoint = state["checkpoints"][next_index]

        state["current_checkpoint"] = next_checkpoint

        state["messages"].append(
            f"Moving to: {next_checkpoint['title']}"
        )

        print(f"\nNext checkpoint: {next_checkpoint['title']}")
        state["retry_count"] = 0

    return state