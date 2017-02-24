from graphics_helper.graphics import transform_image

image_path = transform_image("example.png", 50, 50, "jpg", ".", encoded=False)
image_base64 = transform_image("example.png", 50, 50, "jpg", ".")
