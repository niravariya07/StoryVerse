import faiss
import numpy as np
import pickle
import os

def build_faiss_index(embeddings, chunks, index_path="faiss_index", dim=384):
    if not os.path.exists(index_path):
        os.makedirs(index_path)

    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)

    faiss.write_index(index, os.path.join(index_path, "index.faiss"))

    with open(os.path.join(index_path, "chunks.pkl"), "wb") as f:
        pickle.dump(chunks, f)

    print(f"FAISS index and chunks saved to '{index_path}'.")