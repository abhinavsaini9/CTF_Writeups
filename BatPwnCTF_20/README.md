# CRfuckPhuck
Miscellaneous

![What is it ](./CRfuckPhuck/CRfuckPhuck.jpg)


We are provided with a file [flag](./CRfuckPhuck/flag) which have no extensions and is corrupted in some sort. After using most of the tools I was not able to find anything. Then we looked at the Hexdump of file and found a file flag.zip and a corrupted png header at the last reversed. 

![hex1](./CRfuckPhuck/Hex1.jpg) ![hex2](./CRfuckPhuck/Hex2.jpg) 

The whole hex was reveresed using 

	$ <flag xxd -p -c1 | tac | xxd -p -r > reverse 

found the reveresed file [reverse](./CRfuckPhuck/reverse). 

After using foremost we found a password locked zip file [zip](./CRfuckPhuck/output/temp.zip) which contained a flag.zip file.
Correcting the header of reverse file gave me a png image 

![png](./CRfuckPhuck/pass.png) 

which had the password "B@TN00t@Fl@g" for the zip file.

After extracting and unzipping flag.zip we get a folder named flagchunks having 116 png images numbered from 0. 
![chunks](./CRfuckPhuck/chunks.jpg)

After fiddling for some time I found that after using stegosolve tool on these images there is some text in their Red Plane. 

![red](./CRfuckPhuck/44.png)

After some researching I found it was a part of Alphuck Esolang programming language (!Hint in Description regarding Alphucking Language). Therefore we had to arrange the image in the order of no. in them and then using the combined text after extracting red plane of images we will get an Alphuck Code.

To correctly order the images according to the number in them I wrote a scipt [OCR](./CRfuckPhuck/output/ocr.py). 

```python

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

```

Code [lsbred](./CRfuckPhuck/lsbred.py) to automate extraction of red plane of each file in correct order.

![Red](./CRfuckPhuck/alphuck.jpg)

Combine all the text to form the Alphuck program you can automate it using OCR but for now I just joined it manually.
	`eeeeeeeeeepaeaeeeaeeeeeeeaeeeeeeeeeeccccisaaaaiijijeeeeeeeeeeeeeeeeeeejiiiijeeeeeeejiiiiiiiiijeeeeeeeeeeeeejceeeeeeeeejceeeeeeeeeeeeeeeeeeeeejaeeejeeeeeeeeeeeeejiiiiiiiiiiiiiiijaiiiiiiiiiiiiiiiiiiijeeeeeeeeeeeeejccjaiiiiijaeeeeeeeej`

Decoded it using [Alphuck](https://www.dcode.fr/alphuck-language).

And the flag is 

`batpwn{O3R_Phu3K}`






 
