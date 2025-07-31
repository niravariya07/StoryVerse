import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def prompt_format(retrieved_chunks, genre):
    context = "\n".join(retrieved_chunks)
    prompt = (
        f"You are a creative storyteller.\n"
        f"Based on the following context, generate a story in the genre of '{genre}'.\n\n"
        f"Context:\n{context}\n\n"
        f"Story:"
    )
    return prompt

def generate_story(retrieved_chunks, genre, model="gpt-3.5-turbo", temperature=0.8, max_tokens=800):
    """
    Use OpenAI's Chat API to generate a story.

    Args:
        retrieved_chunks (list): Relevant context from PDF.
        genre (str): User-selected genre.
        model (str): OpenAI model name.
        temperature (float): Creativity level.
        max_tokens (int): Length of output.

    Returns:
        str: The generated story.
    """
    prompt = prompt_format(retrieved_chunks, genre)

    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful and creative assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=temperature,
        max_tokens=max_tokens
    )

    return response['choices'][0]['message']['content'].strip()