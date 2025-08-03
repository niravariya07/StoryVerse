import streamlit as st
import os
import openai
from dotenv import load_dotenv

load_dotenv()

def get_openai_api_key(max_fallback_uses: int = 5) -> str:
    fallback_key = os.getenv("OPENAI_API_KEY")

    # Input from user (optional)
    user_key = st.text_input("Enter your OpenAI API Key (optional):", type="password")

    # Select which key to use
    if user_key:
        api_key = user_key
        st.success("✅ Using your OpenAI API key.")
    else:
        api_key = fallback_key
        st.warning("⚠️ Using demo access with shared API key.")
        
        # Optional: fallback rate limiting
        if "fallback_count" not in st.session_state:
            st.session_state["fallback_count"] = 0
        if st.session_state["fallback_count"] >= max_fall