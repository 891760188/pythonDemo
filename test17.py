#-*- coding: UTF-8 -*-
import pytesseract
from PIL import Image

image = Image.open('yzm01.png')
vcode = pytesseract.image_to_string(image)
print (vcode)