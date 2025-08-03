import streamlit as st
import os

def get_openai_api_key():
    if "openai_api_key" not in st.session_state:
        st.session_state.openai_api_key = None

    if not st.session_state.openai_api_key:
        st.info("Please enter your OpenAI API Key to continue.")
        api_key_input = st.text_input("🔑 Enter OpenAI API Key", type="password")
        
        if api_key_input:
            st.session_state.openai_api_key = api_key_input
            os.environ["OPENAI_API_KEY"] = api_key_input  # Set it for current runtime
            st.success("API Key saved. You can now generate your story.")
            st.rerun()  # Triggers rerun of the whole script

        st.stop()  # Prevent rest of the app from running
