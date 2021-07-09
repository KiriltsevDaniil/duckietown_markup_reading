#image_cropping.py
import pandas
from PIL import Image
i = 0
k = 1
signs = []
forbidden = ['(1)img-1671__2021-06-13-16-21-33-243335.png',
             '(1)img-1686__2021-06-13-16-21-52-380056.png',
             '(1)img-1681__2021-06-13-16-21-42-703017.png']
data = pandas.read_json("./markup.json", "index")

while i < len(data):
    for key in data["regions"][i].keys():
        signs.append(key)
        
    for sign in signs:
        if "shape_attributes" in data["regions"][i][sign]:
            x_cords = data["regions"][i][sign]["shape_attributes"]["all_points_x"]
            y_cords = data["regions"][i][sign]["shape_attributes"]["all_points_y"]
        else:
            x_cords = data["regions"][i][sign]["shape-attributes"]["all_points_x"]
            y_cords = data["regions"][i][sign]["shape-attributes"]["all_points_y"]
        
        polygon = [min(x_cords), min(y_cords), max(x_cords), max(y_cords)]
        image = Image.open("./" + data["filename"][i], "r")
        cropped_image = image.crop(polygon)
        if f'({k}){data["filename"][i]}' not in forbidden:
            cropped_image.save(f'./new_dataset/({k}){data["filename"][i]}')
        k+=1
    k = 1
    signs = []
    i+=1
print("Dataset cropping complete.")
