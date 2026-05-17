import os
from PIL import Image
import pytesseract
from docx import Document
from src.resume_parser import extract_text_from_pdf


def extract_text(file_path):

    extension = os.path.splitext(file_path)[1].lower()

    # PDF
    if extension == ".pdf":
        return extract_text_from_pdf(file_path)

    # DOCX
    elif extension == ".docx":

        doc = Document(file_path)

        text = []

        for para in doc.paragraphs:
            text.append(para.text)

        return "\n".join(text)

    # IMAGE
    elif extension in [".png", ".jpg", ".jpeg"]:

        image = Image.open(file_path)

        text = pytesseract.image_to_string(image)

        return text

    else:
        return ""