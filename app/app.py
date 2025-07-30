import streamlit as st
from utils.text_extraction_from_pdf import text_extraction_from_text

st.title("Document Text Extraction")
uploaded_file = st.file_uploader("Upload a PDF, DOCX, or TXT file", type=["pdf", "docx", "txt"])

if uploaded_file is not None:
    extracted_text = text_extraction_from_text(uploaded_file)
    st.subheader("Extracted Text")
    st.write(extracted_text)