import os
import pytesseract
from PIL import Image
chunks = os.listdir()
order = []
for i in chunks:
    if i == 'ocr.py':
        continue
    else:
        text = pytesseract.image_to_string(Image.open(i),config = '--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789' , lang = 'eng')
        obj = {'iname':i,'number':int(text)}
        order.append(obj)



print(sorted(order,key = lambda i: i['number']))
