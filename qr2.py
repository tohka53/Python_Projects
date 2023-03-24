import pyqrcode

import png
from PIL import Image

#inserting website name
s = input("Enter your website: ") 
print(s)
url = pyqrcode.create(s)

#saving image
img = "qr-code.png"
url.png(img, scale=10)

#opening image
im=Image.open(img)

#show
im