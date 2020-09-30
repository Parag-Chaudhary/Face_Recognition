# Importing Modules
import face_recognition
import pickle
import cv2
import os

# Setting the working Directory
DIRECTORY = r'D:\Coursera\MLProject\Face Recoginition\Datasets'
CATERGORIES = os.listdir(DIRECTORY)

KNOWN_ENCODINGS = []
KNOWN_NAMES = []
FILENAME = 'Encodings.pkl'

print('Loading Images...')

for names in CATERGORIES:
    path = os.path.join(DIRECTORY,names)
    for img in os.listdir(path):
        img_path = os.path.join(path,img)

        image = face_recognition.load_image_file(img_path)
        color = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# Detecting the faces
        face_locations = face_recognition.face_locations(color)
# Making Encodings
        encodings = face_recognition.face_encodings(color,face_locations)[0]
# Saving the Encodings and the respective name     
        KNOWN_ENCODINGS.append(encodings)
        KNOWN_NAMES.append(names)

print("Serializing Encodings...")
data = {"encodings": KNOWN_ENCODINGS, "names": KNOWN_NAMES}
outfile = open(FILENAME,'wb')
outfile.write(pickle.dumps(data))
outfile.close()
