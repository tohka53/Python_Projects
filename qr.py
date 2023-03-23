import qrcode


# Creamos el objeto QRCode
qr = qrcode.QRCode(version=1, box_size=10, border=5)

# Agregamos la información que queremos codificar
qr.add_data("https://www.instagram.com/luisc.monge/")

# Generamos el código QR
qr.make(fit=True)

# Creamos una imagen del código QR
img = qr.make_image(fill_color="black", back_color="white")

# Guardamos la imagen del código QR
img.save("luica.png")
