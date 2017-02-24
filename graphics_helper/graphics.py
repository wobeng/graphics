import base64
import cStringIO
import uuid

import os
from PIL import Image

import cv2


def detect_face(image_path):
    # Get user supplied values
    casc_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "frontalface.xml"))

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


def transform_image(file_name, width, height, ext, save_dir, face=True, encoded=True):
    img = Image.open(file_name)

    if face:
        face_box = detect_face(file_name)
        img = Image.open(file_name)
        if face_box:
            img2 = img.crop(face_box)
            img = img2

    if width == 0 and height != 0:
        hpercent = (height / float(img.size[1]))
        width = int((float(img.size[0]) * float(hpercent)))
    elif width != 0 and height == 0:
        wpercent = (width / float(img.size[0]))
        height = int((float(img.size[1]) * float(wpercent)))
    elif width == 0 and height == 0:
        width = img.size[0]
        height = img.size[1]

    img = img.resize((width, height), Image.ANTIALIAS)

    image_format = "jpeg" if ext == "jpg" else ext
    image_format = image_format.capitalize()

    if encoded:
        image_buffer = cStringIO.StringIO()
        img.save(image_buffer, format=image_format)
        return base64.b64encode(image_buffer.getvalue())

    output_file = os.path.join(save_dir, str(uuid.uuid4()) + "." + ext)
    img.save(output_file, format=image_format)

    return output_file
