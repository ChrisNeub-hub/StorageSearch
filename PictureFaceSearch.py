import cv2
import os
import shutil

def search_face(folder_path):
    face_folder = os.path.join(folder_path, "pictures with faces 2")
    if not os.path.exists(face_folder):
        os.makedirs(face_folder)

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png"):
                image_path = os.path.join(root, file)
                try: 
                    image = cv2.imread(image_path)
                    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

                    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
                    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=3)

                    if len(faces) > 0:
                        print("Found face in ", image_path)
                        shutil.move(image_path, os.path.join(face_folder, file))
                except Exception:
                    print(Exception)


face_folder = "pictures with faces 2"
folder_path = "E:\\"
search_face(folder_path)