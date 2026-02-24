from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

def load_vector_store(path):
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    return FAISS.load_local(
    path,
    embeddings,
    allow_dangerous_deserialization=True)

def get_retriever(vectorstore):
    return vectorstore.as_retriever(
        search_kwargs={"k": 4}
    )