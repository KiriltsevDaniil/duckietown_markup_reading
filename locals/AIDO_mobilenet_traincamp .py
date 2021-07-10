#импортируем нужные библиотеки
#для форматирования
import os
#для считывания csv файла
import pandas
import torch
#для определения необходимых методов
import torch.nn as nn
#для загрузчика кастомного датасета
from torch.utils.data import Dataset, DataLoader
#для установки точки пути
import torchvision
#для преобразований изображений и конвертации данных в тензоры
import torchvision.transforms as transforms
#для модели MobileNet_v2
import torchvision.models as models
#для обработки изображений
import PIL.Image as Image


#Определяем пути более точно + гиперпараметры
num_epochs = 6 
num_classes = 6 
batch_size = 25 
learning_rate = 0.0001
dataset_path = './dataset'

#функция для перевода текстовых классов в цифровые метки
def target_conv(line):
    targets = ["no-left-turn-1", "T-intersection-1", "right-T-intersection-1", "left-T-intersection-1", "stop-1", "traffic-light-1"]
    i = 0
    for target in targets:
        if target == line:
            return i
        else:
            i+=1
    return 6

#инициализация класса для подачи датасета в сеть
class MyDataset(Dataset):
    def __init__(self, csv_file, root_dir, transform=None):
        self.annotations = pandas.read_csv(csv_file)
        self.root_dir = root_dir
        self.transform = transform

    def __len__(self):
        return len(self.annotations)

    def __getitem__(self, index):
        img_path = os.path.join(self.root_dir, self.annotations.iloc[index, 1])
        image = Image.open(img_path)
        y_label = torch.tensor(int(target_conv(self.annotations.iloc[index, 4]))) 

        if self.transform:
            tr = nn.AdaptiveMaxPool2d(157) 
            image = self.transform(image)
            image = tr(image)
          
        return (image, y_label)

#Приведение к тензорам и нормирование.
transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))]) 
#распределение изображений датасета
dataset = MyDataset(csv_file="./markup.csv", root_dir=dataset_path, transform=transforms.ToTensor())
trainset, testset = torch.utils.data.random_split(dataset, [319,319])
trainloader = DataLoader(dataset=trainset, batch_size=batch_size, shuffle=True)
testloader = DataLoader(dataset=testset, batch_size=batch_size, shuffle=True)

#Загрузка модели
model = models.mobilenet_v2(pretrained=True)
model.classifier[1] = nn.Linear(1280, 6)
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

#Обучение
total_step = len(trainloader)
loss_list = []
acc_list = []
for epoch in range(num_epochs):
    for i, (images, labels) in enumerate(trainloader):
        # Прямой запуск
        print(images.shape)
        outputs = model(images)
        loss = criterion(outputs, labels)
        loss_list.append(loss.item())

        # Обратное распространение и оптимизатор
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        # точность
        total = labels.size(0)
        _, predicted = torch.max(outputs.data, 1)
        correct = (predicted == labels).sum().item()
        acc_list.append(correct / total)

        if (i + 1) % 5 == 0:
            print('Epoch [{}/{}], Step [{}/{}], Loss: {:.4f}, Accuracy: {:.2f}%'
                  .format(epoch + 1, num_epochs, i + 1, total_step, loss.item(),
                          (correct / total) * 100))

#Валидация
model.eval()
with torch.no_grad():
    correct = 0
    total = 0
    for images, labels in testloader:
        outputs = model(images)
        _, predicted = torch.max(outputs.data, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()
#сохранение модели
    print('Test Accuracy of the model on the 318 test images: {} %'.format((correct / total) * 100))
    torch.save(model.state_dict(),"./w{}.pt".format(int(correct / total) * 100))