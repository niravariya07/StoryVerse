# 📖 StoryVerse - PDF to Story Generator

**StoryVerse** is an AI-powered storytelling app that transforms your uploaded PDFs into creative stories across genres like **Fantasy**, **Sci-Fi**, **Romance**, **Mystery**, and more — all in a few clicks!

🔗 **Live App**: [storyverse.streamlit.app](https://storyverse-nmj2hdhk4uttudtxfidayg.streamlit.app/)

---

## ✨ Features

- 📄 Upload any **PDF** – extract meaningful text effortlessly  
- 🧠 **AI-Powered Storytelling** – generate engaging stories using modern NLP techniques  
- 🎭 Choose a **Genre** – Fantasy, Horror, Romance, Adventure, and more  
- 💾 Download your story as `.txt` 
- ⚡ Built with **Streamlit**, **FAISS**, and **SentenceTransformers**

---

## 🚀 How It Works

1. **Upload a PDF**  
2. **Text is extracted** from your file using PyMuPDF  
3. Text is **chunked and embedded** using `all-MiniLM-L6-v2`  
4. **FAISS retrieves** the most relevant chunks based on your input  
5. An **LLM generates** a genre-specific story  
6. Story is **displayed and downloadable** as `.txt` or `.pdf`

---

## 🛠️ Tech Stack

- **Frontend**: [Streamlit](https://streamlit.io/)  
- **Embeddings**: [SentenceTransformers](https://www.sbert.net/)  
- **Vector Search**: [FAISS](https://github.com/facebookresearch/faiss)  
- **PDF Parsing**: [PyMuPDF](https://pymupdf.readthedocs.io/)  
- **Language Model**: OpenAI / Gemini (customizable)

---

## 📂 Project Structure

