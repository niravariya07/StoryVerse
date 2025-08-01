import os
import tempfile
import streamlit as st
from utils.build_index import build_faiss_index
from utils.chunks import chunk_text
from utils.embeddings_ import embed_text
from utils.retriever import retrieve_similar_chunks
from utils.story_generator import story_generator_llm
from utils.text_extraction_from_pdf import text_extraction_from_pdf

st.set_page_config(page_title="StoryVerse", layout="centered")
st.title("StoryVerse - PDF to Story Generator")
st.write("Upload a PDF and choose a genre to generate a story using AI.")

uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])

genre = st.selectbox("Choose a genre",
                     ["Fantasy", "Sci-Fi", "Horror", "Romance", "Mystery", "Adventure", "Comedy", "Drama"])

if uploaded_file and genre:
    if st.button("Generate Story"):
        with st.spinner("Extracting text from PDF...."):
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
                tmp_file.write(uploaded_file.read())
                tmp_path = tmp_file.name

        extracted_text = text_extraction_from_pdf(tmp_path)
        os.unlink(tmp_path)

    if not extracted_text.strip():
        st.error("Failed to extract text. Try with a different PDF.")
    else:
        with st.spinner("Chunking and embedding text...."):
            chunks = chunk_text(extracted_text)
            embeddings = embed_text(chunks)
            faiss_index = build_faiss_index(embeddings, chunks)

        with st.spinner("Retriving relevant chunks...."):
            retrieved_chunks = retrieve_similar_chunks(faiss_index, chunks, genre)

        with st.spinner("Generating story...."):
            story = story_generator_llm(retrieved_chunks,genre)
        st.success("Story generated")
        st.header("Your Story")
        st.write(story)