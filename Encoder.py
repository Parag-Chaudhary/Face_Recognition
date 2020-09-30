import face_recognition
import pickle
import cv2
import os

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

        face_locations = face_recognition.face_locations(color)
        encodings = face_recognition.face_encodings(color,face_locations)[0]
        #(BECAUSE WE WANT THAT EVERY IMAGE ENCODINGS MUST BE AT 0 INDEX OF encodings SO THAT SINGLE
        # ENCODING WILL APPEND IN THIS knownEncodings....BUT IS DONT USE [0] THEN NEXT ENCODINGS WILL AT
        # THE NEXT POSTION OF THE encodings WHILE PREVIOUS WILL THERE ALSO)

        # # loop over the encodings  ( ALSO DO THIS IF WE DID NOT WANT [0] )
        # for encoding in encodings:
        #     # add each encoding + name to our set of known names and
        #     # encodings
        #     knownEncodings.append(encoding)
        #     knownNames.append(name)

        KNOWN_ENCODINGS.append(encodings)
        KNOWN_NAMES.append(names)

print("Serializing Encodings...")
data = {"encodings": KNOWN_ENCODINGS, "names": KNOWN_NAMES}
outfile = open(FILENAME,'wb')
outfile.write(pickle.dumps(data))
outfile.close()