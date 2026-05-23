def retrieve_context(vectorstore, query):

    docs = vectorstore.similarity_search(
        query,
        k=2
    )

    context = "\n".join(
        [doc.page_content for doc in docs]
    )

    return context
