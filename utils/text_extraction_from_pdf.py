import tempfile
import fitz
import docx2txt
import os
import io

def text_extraction_from_text(uploaded_file):
    file_name = uploaded_file.name
    file_type = file_name.split('.')[-1].lower()
    print(f"File uploaded: {file_name}, Type: {file_type}")

    uploaded_file.seek(0)
    try:
        file_content = uploaded_file.read()
        print(f"First 500 bytes of file content: {file_content[:100]}")
    except Exception as e:
        print(f"Error reading file content: {e}")
        raise ValueError(f"Error reading file: {e}")

    if file_type == "pdf":
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
            tmp_file.write(file_content)
            tmp_path = tmp_file.name
            print(f"Temporary PDF file created at: {tmp_path}")

        try:
            doc = fitz.open(tmp_path)
            text = ""
            for page in doc:
                text += page.get_text()
            doc.close()
            os.remove(tmp_path)

            print(f"Extracted text from PDF: {text[:200]}")
        except Exception as e:
            print(f"Error extracting text from PDF: {e}")
            raise ValueError(f"Error extracting text from PDF: {e}")

    elif file_type == "docx":
        temp_bytes = io.BytesIO(file_content)
        text = docx2txt.process(temp_bytes)
        print(f"Extracted text from DOCX: {text[:200]}")

    elif file_type == "txt":
        text = file_content.decode('utf-8')
        print(f"Extracted text from TXT: {text[:200]}")

    else:
        print("Unsupported file type.")
        raise ValueError("Unsupported file type! Please upload a PDF, DOCX, or TXT file.")

    return text