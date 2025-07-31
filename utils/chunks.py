# chunks.py

from nltk.tokenize import sent_tokenize

def chunk_text(text, max_words=100, overlap=20):
    """
    Splits text into overlapping chunks of sentences, each with a limit on word count.

    Args:
        text (str): The full extracted text.
        max_words (int): Maximum number of words per chunk.
        overlap (int): Number of words to overlap between chunks.

    Returns:
        List[str]: A list of text chunks.
    """
    sentences = sent_tokenize(text)
    chunks = []
    current_chunk = []

    total_words = 0

    for sent in sentences:
        words = sent.split()
        if total_words + len(words) <= max_words:
            current_chunk.extend(words)
            total_words += len(words)
        else:
            chunks.append(' '.join(current_chunk))

            if overlap > 0:
                current_chunk = current_chunk[-overlap:]
                total_words = len(current_chunk)
            else:
                current_chunk = []
                total_words = 0

            current_chunk.extend(words)
            total_words += len(words)

    if current_chunk:
        chunks.append(' '.join(current_chunk))

    return chunks