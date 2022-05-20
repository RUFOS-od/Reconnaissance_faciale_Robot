# nous allons debuter le systeme de reconnaissance faciale 

#####################################################################################################################################

## nous allons faire nôtre importation de nos fichier et par la suite 

import cv2
import face_recognition
img = cv2.imread("charo.jpeg")# nous venons de charger nôtre image pour nous faciliter la reconnaissance faciale .
# nous allons convertir le format de l'image en rgb 
rgb_img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
# nous allons pas la suite passer a l'encodage e nôtre image.
img_encoding = face_recognition.face_encodings(rgb_img)[0]
##################################################################################################################
img2 = cv2.imread("aristide.jpeg")# nous venons de charger nôtre image pour nous faciliter la reconnaissance faciale .
# nous allons convertir le format de l'image en rgb 
rgb_img2 = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
# nous allons pas la suite passer a l'encodage e nôtre image.
img_encoding2 = face_recognition.face_encodings(rgb_img2)[0]


result = face_recognition.compare_faces([img_encoding], img_encoding2)
print("Result: ", result)# nous affaire un print de notre programme. 
cv2.imshow("Img",img)# nous allons faire afficher nôtre  image 1 .
cv2.imshow("Img 2",img2)# nous allons faire afficher nôtre  image 2.
cv2.waitKey(0)# nous venons d' afficher l'image  tout en maintenant la fénêtre.
