#new_markup.py
import pandas
from PIL import Image
i = 0
k = 1
signs = []
legend = ["name", "width", "height", "class"]
new_data = []
forbidden = ['(1)img-1671__2021-06-13-16-21-33-243335.png',
             '(1)img-1686__2021-06-13-16-21-52-380056.png',
             '(1)img-1681__2021-06-13-16-21-42-703017.png']

data = pandas.read_json("./markup.json", "index")

while i < len(data):
    for key in data["regions"][i].keys():
        signs.append(key)
        
    for sign in signs:
        if f'({k}){data["filename"][i]}' not in forbidden:
            image = Image.open(f'./new_dataset/({k}){data["filename"][i]}', "r")
            w, h = image.size
            new_data.append([f'({k}){data["filename"][i]}', w, h, sign])
        k+=1
    k = 1
    signs = []
    i+=1
df = pandas.DataFrame(new_data, columns=legend)
df.to_csv("./new_dataset/markup.csv")
print("Dataset markup complete.")
