
from unicodedata import name
import cv2

from simple_facerec import SimpleFacerec



sfr = SimpleFacerec()
sfr.load_encoding_images("images/")

def show_webcam(mirror=False):
    cam = cv2.VideoCapture(0)
    while True:
        ret_val, img = cam.read()
        
        if mirror: 
            img = cv2.flip(img, 1)
            face_locations, face_names = sfr.detect_known_faces(img)
            for face_loc, name in zip(face_locations,face_names):
                y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]
                cv2.putText(img, name,(x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 0), 2)
                cv2.rectangle(img, (x1, y1), (x2, y2), (0,128,0), 4)
        cv2.imshow('ma camera', img)
        if cv2.waitKey(1) == 27: 
            break  # esc pour quitté le frame .
    cv2.destroyAllWindows()


def main():
    show_webcam(mirror=True)


if __name__ == '__main__':
    main()