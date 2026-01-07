
from functools import lru_cache
from langchain_community.vectorstores import Chroma
from src.runtime.embedding_model import get_embedding_model

@lru_cache
def get_vector_store():
    vector_store = Chroma(
        collection_name="financial_collection",
        persist_directory="vector_db",
        embedding_function=get_embedding_model()
    )
    return vector_store
