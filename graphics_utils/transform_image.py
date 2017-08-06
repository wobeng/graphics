import uuid

from graphics_utils import detect_face
import os
from PIL import Image


def transform_image(file_name, width, height, ext, save_dir, face=True):
    img = Image.open(file_name)

    if face:
        face_box = detect_face.detect_face(file_name)
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

    output_file = os.path.join(save_dir, str(uuid.uuid4()) + "." + ext)
    img.save(output_file, format=image_format)

    return output_file
