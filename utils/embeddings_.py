from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')

def embed_text(chunks):
    embeddings = model.encode(chunks, show_progress_bar=True)
    return np.array(embeddings)