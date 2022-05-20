# coding utf8

import cv2
import os
import time
import numpy as np 
from unicodedata import name

cam = cv2.VideoCapture(0)
cv2.namedWindow("test")
nom = input("veuillez saisir vôtre nom ")
 
while True:
    ret, frame = cam.read()
    
    
    if not ret:
        print("n'a pas réussi à saisir le cadre")
        break
    cv2.imshow("Selectionne l'ecran Appuyer sur la touche espace pour demarer la capture ", frame)
 
    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("vous venez de fermer la capture !!!")
        break 
    elif k%256 == 32:
        # SPACE pressed
        cv2.imshow('img',  frame)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('img',frame)
        img_name = f"{nom}.png"
        cv2.imwrite(img_name, frame)
        time.sleep(2.4)
        cv2.imshow("capture de image  effectuer avec succes ", frame)
        time.sleep(2.4)
        print("{} capture effectuer avec succès".format(img_name))
        
        
 
cam.release()
 
cv2.destroyAllWindows()