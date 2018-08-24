import os

from graphics_utils import cv2


def detect_face(image_path):
    # Get user supplied values
    casc_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'frontalface.xml'))

    # Create the haar cascade
    face_cascade = cv2.CascadeClassifier(casc_path)

    # Read the image
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
        # flags = cv2.CV_HAAR_SCALE_IMAGE
    )

    for (x, y, w, h) in faces:
        y -= h * 0.3
        h *= 1.6
        x -= w * 0.3
        w *= 1.6
        return x, y, x + w, y + h

    return None
