import dlib
import face_recognition
import cv2


detector = dlib.get_frontal_face_detector()


emre = face_recognition.load_image_file("emre.jpeg")
emre_encodings = face_recognition.face_encodings(emre)


if len(emre_encodings) > 0:
    emre_enc = emre_encodings[0]
else:
    print("HATA: 'emre.jpeg' resminde yüz tespit edilemedi!")
    exit()


cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    faces = detector(rgb_frame)

    face_locations = []
    for face in faces:
        x = face.left()
        y = face.top()
        w = face.right()
        h = face.bottom()
        face_locations.append((y, w, h, x,))

    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    for i, face in enumerate(face_encodings):
        y, w, h, x = face_locations[i]

        result = face_recognition.compare_faces([emre_enc], face)

        if any(result):
            cv2.rectangle(frame, (x, y), (w, h), (0, 255, 0), 2)
            cv2.putText(frame, "Emre", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        else:
            cv2.rectangle(frame, (x, y), (w, h), (0, 0, 255), 2)
            cv2.putText(frame, "Stranger", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.imshow('Yüz Tanıma Sistemi', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
