
# coding utf-8
### nous allons faire l'importattion des modeules 
from PIL import Image, ImageDraw
import face_recognition
import numpy as np

# Chargez un exemple d'image et apprenez a la reconnaitre
image_aristide = face_recognition.load_image_file("aristide.jpeg")
encodage_visage_aristide = face_recognition.face_encodings(image_aristide)[0] ## importations des autres images 
image_charo = face_recognition.load_image_file("charo.jpeg")
encodage_visage_charo = face_recognition.face_encodings(image_charo)[0] ## importations des deux images 
#########################################################################################################################

# Creer une liste d'encodages de visage connus et leurs noms
encodage_visage_connu = [
    encodage_visage_aristide,
    encodage_visage_charo
]
nom_visage_connu = [
    "Irié aristide ",
    "charo"
]
##########################################################################################################################
# Charger une image avec un visage inconnu
image_inconnu = face_recognition.load_image_file("dialo.jpeg") # ici nous allons charger le visage de dialo 

# Trouver tous les visages et encodages de visage dans l'image inconnue
emp_visage_inconnu = face_recognition.face_locations(image_inconnu)
encodage_visage_inconnu = face_recognition.face_encodings(image_inconnu, emp_visage_inconnu)

image_pil = Image.fromarray(image_inconnu)
draw = ImageDraw.Draw(image_pil)

# Traverser chaque visage trouve dans l'image inconnue
for (haut, droite, bas, gauche), encodage_visage in zip(emp_visage_inconnu, encodage_visage_inconnu):
    # Voir si le visage correspond au visage connu
    corresp = face_recognition.compare_faces(encodage_visage_connu, encodage_visage)
    # [True, False]
    
    nom = "Inconnu dans nôtre affaire de robot la!!!"

    # Ou a la place, utilisez le visage connu avec la plus petite distance par rapport au nouveau visage
    distances_visages = face_recognition.face_distance(encodage_visage_connu, encodage_visage)
    meilleur_indice = np.argmin(distances_visages)
    if corresp[meilleur_indice]:
        nom = nom_visage_connu[meilleur_indice]

    # Dessinez une boite autour du visage a l'aide du module Pillow
    draw.rectangle(((gauche, haut), (droite, bas)), outline=(0, 0, 255))

    # Dessinez une etiquette avec un nom sous le visage
    largeur_texte, hauteur_texte = draw.textsize(nom)
    draw.text((gauche + 6, bas - hauteur_texte - 5), nom, fill=(255, 255, 255, 255))


# Afficher l'image resultante
image_pil.show()
image_pil.save("im2.jpg") #- Enregistrer l'image dans un fichier image .jpg