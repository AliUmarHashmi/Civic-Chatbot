from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from config import VECTOR_DB_PATH
from rag.embeddings import get_embeddings


def get_docs(query):
    embeddings = get_embeddings()
    db = FAISS.load_local(
    VECTOR_DB_PATH,
    embeddings,
    allow_dangerous_deserialization=True
)

    docs = db.similarity_search(query, k=3)

    return docs