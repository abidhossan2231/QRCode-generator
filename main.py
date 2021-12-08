import pyqrcode
import png
from pyqrcode import QRCode

# String which represents the QR code
qr = "https://abidhossan2231.yolasite.com/"

# Generate QR code
url = pyqrcode.create(qr)

url.svg("pbQR.svg", scale=8)

url.png('pbQR.png', scale=6)
