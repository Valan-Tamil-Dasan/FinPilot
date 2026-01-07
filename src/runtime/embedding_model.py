from functools import lru_cache
from langchain_huggingface import HuggingFaceEmbeddings


@lru_cache
def get_embedding_model():
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
    return embeddings
