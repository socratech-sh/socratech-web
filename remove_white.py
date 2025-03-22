from PIL import Image
from typing import Tuple

RGB = Tuple[int]


def replace_pixel(image_path, output_path, value1: RGB, value2: RGB):
    img = Image.open(image_path)
    img = img.convert("RGBA")
    datas = img.getdata()
    new_data = []
    for item in datas:
        print(item[:3])
        if item[:3] == value1:
            new_data.append(value2)
        else:
            new_data.append(item)
    img.putdata(new_data)
    img.save(output_path, "PNG")

