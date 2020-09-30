import face_recognition
import pickle
import cv2

print('Loading Encodings...')
data = pickle.loads(open('Encodings.pkl','rb').read())

print("Starting Video Stream...")
cap = cv2.VideoCapture(0)

# fourcc = cv2.VideoWriter_fourcc(*'XVID')
# out = cv2.VideoWriter('Final.avi', fourcc, 5.0, (640, 480))

while True:
    ret, frame = cap.read()
    color = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    face_locations = face_recognition.face_locations(color)  # model="cnn" (by default it's model="hog"
    encodings = face_recognition.face_encodings(color,face_locations)
    names = []
    for encoding in encodings:
        matches = face_recognition.compare_faces(data['encodings'],encoding)
        name='Unknown'

        if True in matches:
            matchedIdxs = [i for (i, b) in enumerate(matches) if b]
            counts = {}
            # loop over the matched indexes and maintain a count for
            # each recognized face face
            for i in matchedIdxs:
                name = data["names"][i]
                counts[name] = counts.get(name, 0) + 1
            # determine the recognized face with the largest number
            # of votes (note: in the event of an unlikely tie Python
            # will select first entry in the dictionary)
            name = max(counts, key=counts.get)
            # update the list of names
        names.append(name)

    for ((top, right, bottom, left), name) in zip(face_locations, names):
        cv2.rectangle(frame, (left, top), (right, bottom), (255, 255, 255), 2)
        cv2.putText(frame,name,(left,top-10),cv2.FONT_HERSHEY_SIMPLEX,0.75, (255, 255, 255), 2)

        # out.write(frame)

    cv2.imshow('CAMERA', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()