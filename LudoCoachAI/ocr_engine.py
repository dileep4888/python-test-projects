from PIL import Image
import pytesseract

def extract_board_state(image_path):
    image = Image.open(image_path)
    raw_text = pytesseract.image_to_string(image)
    return raw_text.strip()
