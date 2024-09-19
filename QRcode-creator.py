import qrcode
import os

# Chemin où l'image sera enregistrée (jsp pk mais il me le mets à la racine ce fdpdf)
chemin_image = "C:/Users/Ethan B/OneDrive - Reseau-GES/Bureau/test"

# Créer un QR code avec le texte 
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data("J'ai ton ip 🥺")
qr.make(fit=True)

# Créer une image QR code (avec les couleur de base(oui oui tu mets "red" à la place de black ça marche))
# color1 = "black"
# color2 = "white"

color1 = "green"
color2 = "cyan"
img = qr.make_image(fill_color=color1, back_color=color2)

# Sauvegarder l'image QR code
nom_image = "qrcode_ilestbo.png"
chemin_complet_image = os.path.join(chemin_image, nom_image)
img.save(chemin_complet_image)

print("QR code généré avec succès!")
