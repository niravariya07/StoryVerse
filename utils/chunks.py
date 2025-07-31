from sentence_transformers import SentenceTransformer
from transformers import AutoTokenizer

def chunk_text(text, model_name="all-MiniLM-L6-v2", max_tokens=512, overlap=50):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    tokens = tokenizer.encode(text, add_special_tokens=False)

    chunks = []
    start = 0
    
    while start < len(tokens):
        end = start + max_tokens
        chunk_tokens = tokens[start:end]
        chunk_text = tokenizer.decode(chunk_tokens, skip_special_tokens=True)
        chunks.append(chunk_text)
        start += max_tokens - overlap

    return chunks