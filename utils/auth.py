import streamlit as st
import os
from dotenv import load_dotenv
import openai

load_dotenv()

def get_openai_api_key(max_fallback_uses: int = 5) -> str:
    fallback_key = os.getenv("OPENAI_API_KEY")

    with st.expander("🔐 Use your own OpenAI API Key (optional)"):
        user_key = st.text_input("Paste your OpenAI key here:", type="password", placeholder="sk-...", key="user_input_key")
        st.markdown("[Don't have one? Get it here](https://platform.openai.com/account/api-keys)")

        if user_key:
            st.session_state["api_key"] = user_key
            st.session_state["using_fallback"] = False
        elif "api_key" not in st.session_state:
            st.session_state["api_key"] = fallback_key
            st.session_state["using_fallback"] = True

    api_key = st.session_state["api_key"]

    if st.session_state.get("using_fallback", False):
        if "fallback_count" not in st.session_state:
            st.session_state["fallback_count"] = 0
        if st.session_state["fallback_count"] >= max_fallback_uses:
            st.error("🚫 Demo limit reached. Please enter your own API key to continue.")
            st.stop()
        else:
            st.session_state["fallback_count"] += 1

    if "api_validated" not in st.session_state:
        try:
            openai.api_key = api_key
            openai.Model.list()
            st.session_state["api_validated"] = True
        except Exception:
            st.error("❌ Invalid or unauthorized API key.")
            st.stop()

    return api_key