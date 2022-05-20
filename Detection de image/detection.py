#nous allons commencer a faire la detection de image dans nôtre programme 


######################################################################################

# Debut de programme
######################################################################################


import face_recognition
from PIL import Image, ImageDraw

image = face_recognition.load_image_file("aristide.jpeg") # Chargez l'image

loc = face_recognition.face_locations(image) # Détecter les visages

# Créer une nouvelle image
image_pil = Image.fromarray(image)
draw = ImageDraw.Draw(image_pil)

# Dessinez les carrés
for tete in loc:
    y0, x0, y1, x1 = tete
    draw.rectangle(((x0, y0), (x1, y1)), outline=(0,0,255))

# Afficher la nouvelle image
image_pil.show()


