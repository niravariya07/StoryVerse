import tempfile
import fitz
import docx2txt
import os
import io

def text_extraction_from_pdf(pdf_path):

    try:
        doc = fitz.open(pdf_path)
        text = ""
        for page in doc:
            text += page.get_text()
        doc.close()
        return text.strip()

    except Exception as e:
        print(f"[Error] Failed to extract text from PDF: {e}")
        return ""

