import qrcode
import os

# Here is the folder where its save
chemin_image = "C:/Users/"

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data("Put right here the text you want")
qr.make(fit=True)

# Here is the clasic color
# color1 = "black"
# color2 = "white"

color1 = "green"
color2 = "cyan"
img = qr.make_image(fill_color=color1, back_color=color2)

# Save the image as a png
nom_image = "qrcode.png"
chemin_complet_image = os.path.join(chemin_image, nom_image)
img.save(chemin_complet_image)

print("QR code généré avec succès!")
