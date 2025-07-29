import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize

def chunk_text(text, max_tokens=500, overlap=50):
    """
    Splits input text into chunks based on sentence boundaries, controlling for token limits and overlap.
    
    Parameters:
    - text (str): The full input text (e.g., from a PDF).
    - max_tokens (int): Maximum tokens per chunk (approximate, using word count).
    - overlap (int): Number of tokens to overlap between chunks for context continuity.

    Returns:
    - List[str]: List of text chunks.
    """
    sentences = sent_tokenize(text)
    chunks = []
    current_chunk = []
    current_length = 0

    for sentence in sentences:
        sentence_length = len(sentence.split())

        if current_length + sentence_length > max_tokens:
            # Save current chunk
            chunks.append(" ".join(current_chunk))

            # Overlap: take last few sentences
            overlap_tokens = []
            overlap_count = 0
            for sent in reversed(current_chunk):
                overlap_tokens.insert(0, sent)
                overlap_count += len(sent.split())
                if overlap_count >= overlap:
                    break

            current_chunk = overlap_tokens
            current_length = sum(len(s.split()) for s in current_chunk)

        current_chunk.append(sentence)
        current_length += sentence_length

    # Add final chunk
    if current_chunk:
        chunks.append(" ".join(current_chunk))

    return chunks