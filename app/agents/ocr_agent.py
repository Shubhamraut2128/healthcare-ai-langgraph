import pytesseract

from PIL import Image


pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)


def ocr_agent(state):

    image_path = state["file_path"]

    image = Image.open(image_path)

    extracted_text = pytesseract.image_to_string(image)

    return {
        "extracted_text": extracted_text
    }