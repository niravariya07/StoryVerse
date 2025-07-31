import faiss
import numpy as np
import pickle
import os

def build_faiss_index(embeddings, chunks, index_path="faiss_index", dim=384):
    