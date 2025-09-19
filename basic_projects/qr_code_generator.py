# In this project we generate a QR CODE from any link

import qrcode as qr

img = qr.make("https://www.youtube.com/@Thekohistani")

img.save("Kohistani.png")