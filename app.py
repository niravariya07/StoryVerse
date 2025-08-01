import os
import tempfile
import streamlit as st
from utils.text_extraction_from_pdf import text_extraction_from_text

st.set_page_config(page_title="StoryVerse", layout="centered")
st.title("StoryVerse - PDF to Story Generator")
st.write("Upload a PDF and choose a genre to generate a story using AI.")

uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])

genre = st.selectbox("Choose a genre",
                     ["Fantasy", "Sci-Fi", "Horror", "Romance", "Mystery", "Adventure", "Comedy", "Drama"])

if uploaded_file and genre:
    if st.button("Generate Story"):
        with st.spinner("Extracting text from PDF...."):
            with tempfile.NamedTEmporaryFile(delete=False, suffix=".pdf") as tmp_file:
                tmp_file.write(uploaded_file.read())
                tmp_path = tmp_file.name

        extracted_text = text_extraction_from_text(tmp_path)
        os.unlink(tmp_path)