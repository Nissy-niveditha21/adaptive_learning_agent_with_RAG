import re


class SimpleVectorStore:

    def __init__(self, documents):
        self.documents = documents

    def similarity_search(self, query, k=2):
        query_tokens = set(re.findall(r"\w+", query.lower()))

        def score(doc):
            text = doc.page_content.lower()
            return sum(1 for token in query_tokens if token in text)

        sorted_docs = sorted(self.documents, key=score, reverse=True)
        return sorted_docs[:k]


def create_vector_store(chunks):
    return SimpleVectorStore(chunks)
