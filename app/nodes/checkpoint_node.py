def checkpoint_node(state):

    print("\n=== CHECKPOINT NODE ===")

    checkpoint = state["current_checkpoint"]

    state["messages"].append(
        f"Current checkpoint: {checkpoint['title']}"
    )

    print(f"\nCheckpoint: {checkpoint['title']}")

    print("\nObjectives:")

    for obj in checkpoint["objectives"]:
        print(f"- {obj}")

    # fake score for now
    #state["score"] = 0.8

    return state