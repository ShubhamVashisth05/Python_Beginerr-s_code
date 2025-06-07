#install the lib needed
#create a fn that collects a text and converts it to a qrcode
#save the qrcode as an img
#run the fn

import qrcode
def generate_qrcode(text):

    qr = qrcode.QRCode(
        version= 1,
        error_correction= qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(text)
    qr.make(fit = True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qrimage.png")

url = input("Enter the text or url: ")
generate_qrcode(url)
