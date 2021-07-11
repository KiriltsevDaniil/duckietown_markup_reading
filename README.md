# duckietown_markup_reading
**Предварительно** <br />
!!Нужно установить библиотеки pandas, PIL, pytorch, torchvision, os!! <br />
!!На локальной машине нужно запускать скрипты на версии python 3+, pytorch 1.9.0, torchvision 0.10.0, PIL 8.2.0!!<br />

1. **Подготовка датасета** (вырезание участков картинок и создание нового файла разметки) располагаются в папке dataset_preparataion.  <br /> 
1.1 image_cropping.py запускается первым из папки с оригинальным датасетом и json - файлом разметки, вырезает нужные участки. <br /> 
  Полученный датасет сохраняется в папку new_dataset в директории запуска. <br /> 
1.2 new_markup.py запускается вторым (из папки, откда запускался первый скрипт) и размечает новый датасет в файл markup.csv. <br />
  Полученный файл сохраняется там же, где и новый датасет. <br />

2. **Работа с новым датасетом** 
**Ссылка на подготовленный датасет** https://drive.google.com/drive/folders/1-HoHLsJW6sNykZp0lv521HNf5aZnua98?usp=sharing <br />
Перейдя по ссылке, откроется папка на гугл-диске, где содержится уже обрезанный датасет, файл разметки и файл с хорошими весами для сети (На валидации она выдавала точность не меньше 98%). <br />

3. **Тренировка сети** <br />
3.1 **Запуск на локальной машине** <br />
1) Скачать папку по ссылке https://drive.google.com/drive/folders/1-HoHLsJW6sNykZp0lv521HNf5aZnua98?usp=sharing <br />
2) Запустить AIDO_mobilenet_traincamp.py (лежащий в locals) в загруженной папке (cropped_dataset). <br />
3) Программа сохранит полученные веса в папку запуска (cropped_dataset). <br />

3.2 **Google Colaboratory** <br />
1) Перейти по ссылке в Google Drive https://drive.google.com/drive/folders/1-HoHLsJW6sNykZp0lv521HNf5aZnua98?usp=sharing <br />
2) Добавить ярлык на данную папку на главную страницу своего диска. <br />
![image](https://user-images.githubusercontent.com/71724561/125188592-f4ecb200-e23c-11eb-9c52-9c99ff9176c9.png)
3) Перейти в Google Colaboratory по следующей ссылке https://vk.com/away.php?utf=1&to=https%3A%2F%2Fcolab.research.google.com%2Fdrive%2F1r6zixGz_oLTzxbCD6-0tekZAeDyPtgWp%3Fusp%3Dsharing <br />
4) Послледовательно выполнить все ячейки. <br />
5) Программа сохранит полученные веса на главную страницу гугл диска. <br />

4. **Проверка точности**  <br />
1) Перейти по ссылке в Google Drive https://drive.google.com/drive/folders/1-HoHLsJW6sNykZp0lv521HNf5aZnua98?usp=sharing <br />
2) Добавить ярлык на данную папку на главную страницу своего диска. <br />
3) Перейти по ссылке <br />
4) Выполнить последовательно все ячейки. <br />

5. **Работа с обученой сетью**  <br />
5.1 **Запуск на локальной машине** <br />
1) Запустить скрипт sign_classifier из папки locals в директории, где на ходится файл c именем markup.csv (в первой колнке должны располагаться имена изображений), описывающий датасет, находящийся в папке dataset, в директории запуска.  <br />
![image](https://user-images.githubusercontent.com/71724561/125187924-8575c300-e23a-11eb-9417-35526ad5ce26.png)
2) Программа запишет название класса во второю колонку файла markup.csv  <br />

5.2 **Google Colaboratory** <br />
1) Перейти по ссылке в Google Drive https://drive.google.com/drive/folders/1-HoHLsJW6sNykZp0lv521HNf5aZnua98?usp=sharing <br />
2) Добавить ярлык на данную папку на главную страницу своего диска. <br />
3) Создать на главной странице диска папку custom_dataset, где на ходится файл c именем markup.csv (в первой колнке должны располагаться имена изображений), описывающий датасет, находящийся в папке dataset, в директории custom_dataset запуска.  <br />
4) Перейти в Google Colaboratory по следующей ссылке https://colab.research.google.com/drive/12-FBZ08wGlb_WtpEag0mOWccRf-1ULFT <br />
5) Послледовательно выполнить все ячейки. <br />
6) Программа запишет название класса во второю колонку файла markup.csv  <br />
