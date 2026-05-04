import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from config import DOCUMENT_PATH, VECTOR_DB_PATH
from rag.embeddings import get_embeddings

def create_vector_db():
    loader = TextLoader(DOCUMENT_PATH)
    documents = loader.load()

    splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    docs = splitter.split_documents(documents)

    embeddings = get_embeddings()

    db = FAISS.from_documents(docs, embeddings)
    db.save_local(VECTOR_DB_PATH)

    print("Vector DB created!")

if __name__ == "__main__":
    create_vector_db()