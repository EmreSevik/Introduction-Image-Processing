import cv2

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('face.xml')
mouth_cascade = cv2.CascadeClassifier('mouth.xml')

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 7)

    if len(faces) == 0:
        cv2.putText(frame, "Face not detected", (40, 40), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 3)
    else:
        for x, y, w, h in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            roi_gray = gray[y + int(h / 2): y + h, x: x + w]
            mouth = mouth_cascade.detectMultiScale(roi_gray, 1.5, 15)

            if len(mouth) == 0:
                cv2.putText(frame, "Mask Detected", (40, 40), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 3)
            else:
                x1, y1, w1, h1 = sorted(mouth, key=lambda m: m[1], reverse=True)[0]
                cv2.rectangle(frame, (x1 + x, y1 + y + int(h / 2)),
                              (x1 + w1 + x, y1 + h1 + y + int(h / 2)), (0, 0, 255), 3)
                cv2.putText(frame, "No Mask", (40, 40), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 3)

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
