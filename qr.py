import qrcode


# Creamos el objeto QRCode
qr = qrcode.QRCode(version=1, box_size=10, border=5)

# Agregamos la información que queremos codificar
qr.add_data("https://forms.gle/8dR5rSH4fvKBT8tp7")

# Generamos el código QR
qr.make(fit=True)

# Creamos una imagen del código QR
img = qr.make_image(fill_color="black", back_color="white")

# Guardamos la imagen del código QR
img.save("encuensta2.png")
