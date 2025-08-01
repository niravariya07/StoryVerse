import streamlit as st
from utils.text_extraction_from_pdf import text_extraction_from_text

st.set_page_config(page_title="StoryVerse", layout="centered")
st.title("StoryVerse - PDF to Story Generator")
st.write("Upload a PDF and choose a genre to generate a story using AI.")

uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])

