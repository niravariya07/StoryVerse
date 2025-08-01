import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def prompt_format(retrieved_chunks, genre):
    context = "\n".join(retrieved_chunks)
    prompt = (
        f"You are a creative storyteller.\n"
        f"Based on the following context, generate a story in the genre of '{genre}'.\n\n"
        f"Context:\n{context}\n\n"
        f"Story:"
    )
    return prompt

def story_generator_llm(retrieved_chunks, genre, model="gemini-pro", temperature=0.8):
    prompt = prompt_format(retrieved_chunks, genre)

    try:
        model = genai.GenerativeModel(model)
        response = model.generate_content(prompt, generation_config={
            "temperature": temperature,
            "top_p": 1,
            "max_output_tokens": 800,
        })

        return response.text.strip()

    except Exception as e:
        return f"⚠️ Gemini API error: {str(e)}"
