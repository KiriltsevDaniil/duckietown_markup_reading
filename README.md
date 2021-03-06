# duckietown_markup_reading
**Предварительно** <br />
!!Нужно установить библиотеки pandas, PIL, pytorch, torchvision, os!! <br />
!!На локальной машине нужно запускать скрипты на версии python 3+, pytorch 1.9.0, torchvision 0.10.0, PIL 8.2.0!!<br />

1. **Подготовка датасета** (вырезание участков картинок и создание нового файла разметки) располагаются в папке dataset_preparataion.  <br /> 
1.0 Необходимо создать директорию в которой будут распологаться три папки и json-файл, описывающий исходный датасет.  <br />
Папка dataset - директория с исходным датасетом.  <br />
Папка dataset_preparation - директория со скриптами.  <br />
Папка new_dataset - директория в которую будет сохранен обработанный датасет. <br />
![image](https://user-images.githubusercontent.com/71724561/125190918-549c8a80-e248-11eb-8582-fb907693e80c.png)

1.1 image_cropping.py запускается первым из папки dataset_preparation и вырезает нужные участки. <br /> 
  Полученный датасет сохраняется в папку new_dataset. <br /> 

1.2 new_markup.py запускается вторым (из папки, откда запускался первый скрипт) и размечает новый датасет в файл markup.csv. <br />
  Полученный файл сохраняется в директории со старой разметкой. <br />

2. **Работа с новым датасетом** <br />
**Ссылка на подготовленный датасет** https://drive.google.com/drive/folders/1-HoHLsJW6sNykZp0lv521HNf5aZnua98?usp=sharing <br />
Перейдя по ссылке, откроется папка на гугл-диске, где содержится уже обрезанный датасет, файл разметки и файл с хорошими весами для сети (На валидации она выдавала точность не меньше 98%). <br />

3. **Тренировка сети** <br />
3.1 **Запуск на локальной машине** <br />
1) Скачать папку cropped_dataset по ссылке https://drive.google.com/drive/folders/1-HoHLsJW6sNykZp0lv521HNf5aZnua98?usp=sharing <br />
2) Распаковать zip архив.
3) Запустить AIDO_mobilenet_traincamp.py (лежащий в locals) в загруженной папке (cropped_dataset). <br />
![image](https://user-images.githubusercontent.com/71724561/125192439-8c0f3500-e250-11eb-9fb4-868b9112ab6b.png)
4) Программа сохранит полученные веса в папку запуска (cropped_dataset). <br />

3.2 **Google Colaboratory** <br />
1) Перейти по ссылке в Google Drive https://drive.google.com/drive/folders/1-HoHLsJW6sNykZp0lv521HNf5aZnua98?usp=sharing <br />
2) Добавить ярлык на данную папку на главную страницу своего диска. <br />
![image](https://user-images.githubusercontent.com/71724561/125188592-f4ecb200-e23c-11eb-9c52-9c99ff9176c9.png)![image](https://user-images.githubusercontent.com/71724561/125195330-d519b600-e25d-11eb-8e49-8c175fa2434c.png)

3) Перейти в Google Colaboratory по следующей ссылке https://colab.research.google.com/drive/1r6zixGz_oLTzxbCD6-0tekZAeDyPtgWp?usp=sharing <br />
4) Последовательно выполнить все ячейки. <br />
5) Программа сохранит полученные веса на главную страницу гугл диска. <br />

4. **Проверка точности**  <br />
1) Перейти по ссылке в Google Drive https://drive.google.com/drive/folders/1-HoHLsJW6sNykZp0lv521HNf5aZnua98?usp=sharing <br />
2) Добавить ярлык на данную папку на главную страницу своего диска. <br />
3) Перейти по ссылке https://colab.research.google.com/drive/1lKOXPvkCVz7aHJsk8AHWcxJRmVFd1UZU?usp=sharing <br />
4) Выполнить последовательно все ячейки. <br />

5. **Работа с обученой сетью**  <br />
5.1 **Запуск на локальной машине** <br />
1) Скачать файл с весами и добавить в папку, где будет запускаться скрипт.
3) Запустить скрипт sign_classifier из папки locals в директории, где на ходится файл c именем markup.csv (в первой колонке должны располагаться имена изображений), описывающий пользовательский датасет, находящийся в папке dataset, в директории запуска.  <br />
![image](https://user-images.githubusercontent.com/71724561/125187924-8575c300-e23a-11eb-9417-35526ad5ce26.png)
3) Программа запишет название класса во второю колонку файла markup.csv  <br />
*) может возникнуть следующая ошибка, но она ни на что не влияет.  <br />
![image](https://user-images.githubusercontent.com/71724561/125195449-58d3a280-e25e-11eb-95d0-5c027311c3ad.png)


5.2 **Google Colaboratory** <br />
1) Перейти по ссылке в Google Drive https://drive.google.com/drive/folders/1-HoHLsJW6sNykZp0lv521HNf5aZnua98?usp=sharing <br />
2) Добавить ярлык на данную папку на главную страницу своего диска. <br />
3) Создать на главной странице диска папку custom_dataset и положить туда файл c именем markup.csv (в первой колонке должны располагаться имена изображений), в папке dataset должен лежать датасет, который будет классифицироваться.  <br />
![image](https://user-images.githubusercontent.com/71724561/125195376-fa0e2900-e25d-11eb-9e05-d42dee48cf6e.png)
4) Перейти в Google Colaboratory по следующей ссылке https://colab.research.google.com/drive/12-FBZ08wGlb_WtpEag0mOWccRf-1ULFT?usp=sharing <br />
5) Последовательно выполнить все ячейки. <br />
6) Программа запишет название класса во второю колонку файла markup.csv  <br />
