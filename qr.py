import qrcode

# Creamos el objeto QRCode
qr = qrcode.QRCode(version=1, box_size=10, border=5)

# Agregamos la información que queremos codificar
qr.add_data("https://www.amazon.com/-/es/overoles-mezclilla-pantalones-camisetas-sudaderas/dp/B082YW6D3K/?_encoding=UTF8&pd_rd_w=V0MRF&content-id=amzn1.sym.661e4241-e0b9-4f43-97f7-81ad6a9143de&pf_rd_p=661e4241-e0b9-4f43-97f7-81ad6a9143de&pf_rd_r=WNFW7AGA95YYXR8Q501Y&pd_rd_wg=04mYz&pd_rd_r=c6e322f3-13dd-4138-beff-03bcaf49b417&ref_=pd_gw_bmx_gp_kl7s8amn")

# Generamos el código QR
qr.make(fit=True)

# Creamos una imagen del código QR
img = qr.make_image(fill_color="black", back_color="white")

# Guardamos la imagen del código QR
img.save("ama.png")
