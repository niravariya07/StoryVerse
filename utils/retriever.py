import faiss
import numpy as np
import pickle
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

def load_faiss_index(index_path="faiss_index"):
    index = faiss.read_index(f"{index_path}/index.faiss")
    with open(f"{index_path}/chunks.pkl", "rb") as f:
        chunks = pickle.load(f)
    return index, chunks

def retrieve_similar_chunks(query, k=3, index_path="faiss_index"):
    query, index, chunks, top_k=5
    index, chunks = load_faiss_index(index_path)

    query_embedding = model.encode([query])
    query_embedding = np.array(query_embedding).astype("float32")

    distances, indices = index.search(query_embedding, k)
    return [chunks[i] for i in indices[0]]