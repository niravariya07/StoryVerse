import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize

def chunk_text(text, max_tokens=500, overlap=50):
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