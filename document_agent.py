from pypdf import PdfReader
from granite_service import ask_granite


def extract_pdf_text(file_path):
    """
    Extract readable text from a PDF file.
    """

    reader = PdfReader(file_path)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text


def analyze_document(file_path):
    """
    Extract text from a PDF and analyze it using IBM Granite.
    """

    text = extract_pdf_text(file_path)

    if not text.strip():
        return "No readable text was found in the PDF."

    # Limit the amount of text sent to the model
    text = text[:12000]

    prompt = f"""
You are ClimateGuard AI.

Analyze the following environmental or climate-related
document.

DOCUMENT:
{text}

Provide:

1. A short summary.
2. Important climate/environment information.
3. Important risks or problems mentioned.
4. Recommended actions.
5. Important entities, locations or organizations
   mentioned in the document.

Use simple English.

Do not invent information that is not present
in the document.
"""

    return ask_granite(
        prompt,
        max_new_tokens=500,
        temperature=0.2
    )