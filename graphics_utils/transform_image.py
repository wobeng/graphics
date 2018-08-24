import os
import uuid

from PIL import Image

from graphics_utils import detect_face


def calculate_size(orig_width, orig_height, width, height):
    if width == 0 and height != 0:
        height_percent = (height / float(orig_height))
        width = int((float(orig_width) * float(height_percent)))
    elif width != 0 and height == 0:
        width_percent = (width / float(orig_width))
        height = int((float(orig_height) * float(width_percent)))
    elif width == 0 and height == 0:
        width = orig_width
        height = orig_height
    return width, height


def transform_image(file_name, width, height, ext, save_dir, crop=True, img=None):
    img = img or Image.open(file_name)

    if crop:
        if crop is True:
            face_box = detect_face.detect_face(file_name)
            if face_box:
                img = img.crop(face_box)
        else:
            img = img.crop(crop)

    size = calculate_size(img.size[0], img.size[1], width, height)
    img = img.resize(size, Image.ANTIALIAS)

    image_format = 'jpeg' if ext == 'jpg' else ext
    image_format = image_format.capitalize()

    output_file = os.path.join(save_dir, str(uuid.uuid4()) + '.' + ext)
    img.save(output_file, optimize=True, format=image_format, quality=85)

    return output_file
