import pdfplumber
from docx import Document


def extract_text_from_pdf(pdf_path):
    """
    Extract text from PDF resume
    """

    text = ""

    with pdfplumber.open(pdf_path) as pdf:

        for page in pdf.pages:
            extracted_text = page.extract_text()

            if extracted_text:
                text += extracted_text + "\n"

    return text


def extract_text_from_docx(docx_path):
    """
    Extract text from DOCX resume
    """

    doc = Document(docx_path)

    text = ""

    for para in doc.paragraphs:
        text += para.text + "\n"

    return text