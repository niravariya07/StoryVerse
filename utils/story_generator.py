import os
from openai import OpenAI, OpenAIError, RateLimitError
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get API key from environment and validate
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("❌ OPENAI_API_KEY not found in environment variables. Please check your .env file.")

# Initialize OpenAI client
client = OpenAI(api_key=api_key)

# Format the prompt based on retrieved chunks and selected genre
def prompt_format(retrieved_chunks, genre):
    context = "\n".join(retrieved_chunks)
    prompt = (
        f"You are a creative storyteller.\n"
        f"Based on the following context, generate a story in the genre of '{genre}'.\n\n"
        f"Context:\n{context}\n\n"
        f"Story:"
    )
    return prompt

# Generate a story using OpenAI LLM
def story_generator_llm(retrieved_chunks, genre, model="gpt-3.5-turbo", temperature=0.8, max_tokens=800):
    prompt = prompt_format(retrieved_chunks, genre)
    
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful and creative assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=temperature,
            max_tokens=max_tokens
        )
        return response.choices[0].message.content.strip()

    except RateLimitError:
        return "⚠️ Your OpenAI API quota has been exceeded. Please check your billing and usage settings."

    except OpenAIError as e:
        return f"❌ OpenAI API error: {str(e)}"

    except Exception as e:
        return f"❌ Unexpected error: {str(e)}"
