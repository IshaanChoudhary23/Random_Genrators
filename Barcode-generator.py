import qrcode
from PIL import Image

qr=qrcode.QRCode(version=1,error_correction=qrcode.ERROR_CORRECT_H,box_size=10,border=4)
qr.add_data("Paste Your URL here")

qr.make(fit=True)
img=qr.make_image(fill_color="yellow",back_color="blue")
img.save("new_qr.png")