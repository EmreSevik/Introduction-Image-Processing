import cv2
import numpy as np

image = cv2.imread('shapes.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

blurred = cv2.GaussianBlur(gray, (5, 5), 0)
edges = cv2.Canny(blurred, 50, 150)

contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

detected_shapes = []

for contour in contours:
    approx = cv2.approxPolyDP(contour, 0.02 * cv2.arcLength(contour, True), True)
    x, y, w, h = cv2.boundingRect(approx)

    center_x, center_y = x + w // 2, y + h // 2

    if any(abs(cx - center_x) < 10 and abs(cy - center_y) < 10 for cx, cy in detected_shapes):
        continue

    detected_shapes.append((center_x, center_y))


    if len(approx) == 3:
        shape_name = "Triangle"
    elif len(approx) == 4:
        aspect_ratio = float(w) / h
        if 0.95 < aspect_ratio < 1.05:
            shape_name = "Square"
        else:
            shape_name = "Rectangle"
    elif len(approx) > 4:
        shape_name = "Circle"
    else:
        shape_name = "Unknown"


    cv2.drawContours(image, [approx], -1, (0, 255, 0), 2)
    cv2.putText(image, shape_name, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

cv2.imshow("Detected Shapes", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
