import qrcode
from io import BytesIO

def generate_qr(phone_number: str) -> BytesIO:
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(f"tel:{phone_number}")
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img_byte_array = BytesIO()
    img.save(img_byte_array, format="PNG")
    return img_byte_array