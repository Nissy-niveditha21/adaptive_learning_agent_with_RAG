import app.rag.initialize as rag_init


def retrieve_context(state):

    print("\n=== RETRIEVER NODE ===")

    checkpoint = state["current_checkpoint"]

    query = " ".join(checkpoint["objectives"])

    docs = rag_init.vectorstore.similarity_search(
        query,
        k=2
    )

    context = "\n".join([
        doc.page_content for doc in docs
    ])

    print("\nRetrieved Context:\n")
    print(context[:500])

    state["retrieved_context"] = context

    return state