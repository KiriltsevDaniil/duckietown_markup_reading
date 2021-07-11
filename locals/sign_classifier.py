"""sign_classifier.ipynb


Original file is located at
    
"""

#импортируем нужные библиотеки
#для считывания csv файла
import pandas
import torch
#для определения необходимых методов
import torch.nn as nn
import torchvision
#для преобразований изображений и конвертации данных в тензоры
import torchvision.transforms as transforms
#для модели MobileNet_v2
import torchvision.models as models
#для обработки изображений
import PIL.Image as Image

#Объявляем путь, где хранятся датасет и csv файл
dataset_path = './dataset/'

#Загрузка модели с хорошими весами
model = models.mobilenet_v2()
model.classifier[1] = nn.Linear(1280, 6)
model.load_state_dict(torch.load("./w(mobile_net)98.12.pt"))
model.eval()

legend = ["name","class"]
new_data = []
df = pandas.read_csv("./markup.csv")
targets = ["no-left-turn-1", "T-intersection-1", "right-T-intersection-1", "left-T-intersection-1", "stop-1", "traffic-light-1"]

for index in range(len(df)):
    name  = df.iloc[index, 0] 
    img = Image.open(dataset_path + name, "r")
    tr = nn.AdaptiveMaxPool2d(157)
    img = transforms.ToTensor()(img) 
    img = img[None, :, :,:]
    img = tr(img)
    _, predicted = torch.max(model(img).data, 1)
    value = targets[int(predicted)]
    new_data.append([name, value])
new_df = pandas.DataFrame(new_data, columns=legend)
new_df.to_csv("./markup.csv")

