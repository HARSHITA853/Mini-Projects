import qrcode
from PIL import Image,ImageDraw
data=qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4
)
data.add_data("https://www.linkedin.com/in/harshita--saxena/")
data.make(fit=True)
img=data.make_image(fill_color="purple",back_color="white").convert("RGBA")
img.save("linkedinQR.png")
img.show()