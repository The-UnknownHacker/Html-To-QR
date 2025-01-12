import qrcode
import base64

html_content = """Your html content here"""


encoded_html = base64.b64encode(html_content.encode('utf-8')).decode('utf-8')

data_url = f"data:text/html;base64,{encoded_html}"

qr = qrcode.QRCode(
    version=40,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=6,
    border=4,
)

qr.add_data(data_url)
qr.make(fit=True)

img = qr.make_image(fill="black", back_color="white")

img.save("img_name.png")
