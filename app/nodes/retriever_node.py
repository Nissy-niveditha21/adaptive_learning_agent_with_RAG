import app.rag.initialize as rag_init


def retrieve_context(state):

    print("\n=== RETRIEVER NODE ===")

    if rag_init.vectorstore is None:
        print("Vectorstore not initialized, rebuilding...\n")
        rag_init.build_rag_pipeline("data/notes/neural_networks.txt")

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