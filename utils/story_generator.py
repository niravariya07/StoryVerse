import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def prompt_format(retrieved_chunks, genre):
    """
    Combine retrieved context and user-selected genre into a prompt.
    """
    context = "\n".join(retrieved_chunks)
    prompt = (
        f"You are a creative storyteller.\n"
        f"Based on the following context, generate a story in the genre of '{genre}'.\n\n"
        f"Context:\n{context}\n\n"
        f"Story:"
    )
    return prompt