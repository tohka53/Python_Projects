#Import module
import qrcode


print("QR CODE GENERATOR")
a= input("Enter link which you of want to make qr code")
#set QR code parameteres
qr = qrcode.QRCode(
    version = 10,
    box_size = 5,
    border = 1
)
#storing input given into data variable
data = a
qr.add_data(data)
#Generate QR Code
qr.make(fit = True)
#set QR code properties
img = qr.make_image(fill="black",back_color = "white")
#save QR code
img.save("QrCodeImage.png")
