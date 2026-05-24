from app.services.document_loader import load_notes
from app.services.text_chunker import chunk_documents
from app.services.vector_store import create_vector_store
vectorstore = None
def build_rag_pipeline(notes_path):
    global vectorstore
    # 1. Load raw notes
    docs = load_notes(notes_path)

    # 2. Chunk them
    chunks = chunk_documents(docs)

    # 3. Build vector store
    vectorstore = create_vector_store(chunks)

    return vectorstore