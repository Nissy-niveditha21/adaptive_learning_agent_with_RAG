from langchain_community.document_loaders import TextLoader


def load_notes(filepath):

    loader = TextLoader(filepath)

    documents = loader.load()

    return documents