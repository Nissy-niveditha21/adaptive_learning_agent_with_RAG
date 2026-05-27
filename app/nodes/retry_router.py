def retry_or_end(state):

    retry_count = state["retry_count"]

    if retry_count >= 3:

        print("\nMaximum retries reached.")

        return "end"

    return "retry"