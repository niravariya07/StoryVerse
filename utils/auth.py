import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()  # Load your .env if it exists

def get_openai_api_key():
    # If already set, skip prompt
    if "openai_api_key" in st.session_state and st.session_state.openai_api_key:
        os.environ["OPENAI_API_KEY"] = st.session_state.openai_api_key
        return

    st.info("🔑 Enter your OpenAI API key or use a limited default key provided by the app.")

    # Option 1: Enter custom key
    api_key_input = st.text_input("Enter OpenAI API Key", type="password")

    # Option 2: Use app's default key
    use_default = st.checkbox("Use default limited-access API key")

    if api_key_input:
        st.session_state.openai_api_key = api_key_input
        os.environ["OPENAI_API_KEY"] = api_key_input
        st.success("✅ API key set successfully.")
        st.rerun()

    elif use_default:
        default_key = os.getenv("OPENAI_API_KEY")
        if default_key:
            st.session_state.openai_api_key = default_key
            os.environ["OPENAI_API_KEY"] = default_key
            st.success("✅ Using default API key.")
            st.rerun()
        else:
            st.error("❌ Default API key not configured in .env file.")

    st.stop()
