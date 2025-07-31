from sentence_transformers import SentenceTransformer
import numpy as np


# # embedder.py

# from sentence_transformers import SentenceTransformer
# import numpy as np

# class Embedder:
#     def __init__(self, model_name='all-MiniLM-L6-v2'):
#         """
#         Initialize the SentenceTransformer model.
#         """
#         self.model = SentenceTransformer(model_name)

#     def embed(self, chunks):
#         """
#         Generate embeddings for each chunk of text.
        
#         Args:
#             chunks (List[str]): List of text chunks.

#         Returns:
#             np.ndarray: Embedding vectors for all chunks.
#         """
#         embeddings = self.model.encode(chunks, show_progress_bar=True)
#         return np.array(embeddings)
