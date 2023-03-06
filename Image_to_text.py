import pytesseract as pt
from PIL import Image
pt.pytesseract.tesseract_cmd = r'C:\Users\asus\AppData\Local\Programs\Tesseract-OCR\tesseract'
img_object = Image.open(r"SAMPLE.jpg")
img_text = pt.image_to_string(img_object)
print(img_text)
