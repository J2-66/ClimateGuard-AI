import io
from pathlib import Path

def extract_file_text(uploaded_file):
    name = uploaded_file.name.lower()
    data = uploaded_file.getvalue()

    if name.endswith(".txt"):
        return data.decode("utf-8", errors="ignore")

    if name.endswith(".pdf"):
        try:
            from pypdf import PdfReader
            reader = PdfReader(io.BytesIO(data))
            return "\n".join((p.extract_text() or "") for p in reader.pages)
        except Exception as e:
            return f"PDF extraction failed: {e}"

    if name.endswith(".docx"):
        try:
            from docx import Document
            doc = Document(io.BytesIO(data))
            return "\n".join(p.text for p in doc.paragraphs)
        except Exception as e:
            return f"DOCX extraction failed: {e}"

    return "Unsupported document."

def extract_image_text(image):
    # Optional OCR. If pytesseract/Tesseract is unavailable, return a useful status.
    try:
        import pytesseract
        return pytesseract.image_to_string(image)
    except Exception:
        return (
            "Image received successfully. OCR is not configured on this machine. "
            "Install pytesseract and the Tesseract OCR engine to extract text from images."
        )
