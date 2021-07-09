# duckietown_markup_reading

<b /> Скрипты для подготовки датасета <b> (вырезание участков картинок и создание нового файла разметки) располагаются в папке dataset_preparataion.
1. image_cropping.py запускается первым и вырезает нужные участки. <br /> 
2. new_markup.py запускается вторым и размечает новый датасет в файл markup.csv. <br />

Ссылка на подготовленный датасет https://drive.google.com/drive/folders/1-HoHLsJW6sNykZp0lv521HNf5aZnua98?usp=sharing <br />
Перейдя по ссылке, откроется папка на гугл-диске, где содержится уже обрезанный датасет, файл разметки и файл с хорошими весами для сети (На тестировании она выдавала точность не меньше 98%). <br />



Проверка точности сети. <br />
Чтобы проверить точность сети, надо в файле AIDO_MobileNet_traincamp.ipynb из папки traincamp_notebook выполнить последовательно все ячейки, пропустив этап обучения.
