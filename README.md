# 4-class Animal Recognition
## Что это за проект? ##
Учебный проект, представляющий собой систему для классификации животных - *носорог, буйвол, зебра, слон* с использованием достаточно простой CNN. Данная модель находится на 2 месте.\
Frontend - **Streamlit** \
Backend - **FastAPI** 

## Описание датасета
[Датасет](https://www.kaggle.com/datasets/ayushv322/animal-classification) состоит из 4 тысяч изображений с различными разрешениями, разделенных на 4 класса.

## Сравниваемые модели

В сравнении участвовали различные модели - от самой простой, использующей векторы - и до дообученной модели ResNet50\
В репозитории также находится блокнот Jupyter, описывающий процесс сравнения моделей

|                            |   inference (10K images) |   accuracy |   recall |   precision |       f1 |
|:---------------------------|-------------------------:|-----------:|---------:|------------:|---------:|
| Trained ResNet (Work 5)    |                 3.15627  |      0.985 |    0.985 |    0.985087 | 0.985005 |
| BN&D (Work 4)              |                 0.319324 |      0.969 |    0.969 |    0.969355 | 0.968882 |
| VGG-like (Work 3)          |                 0.856075 |      0.886 |    0.886 |    0.886254 | 0.885937 |
| Less stupid (Work 3 - own) |                 7.40432  |      0.873 |    0.873 |    0.878983 | 0.873841 |
| Stupid (Work 2)            |                 3.53571  |      0.618 |    0.618 |    0.61793  | 0.613639 |

![image](https://github.com/user-attachments/assets/63462ca6-237c-4556-85b2-2156018a7af5)

## Примеры работы с приложением

![image](https://github.com/user-attachments/assets/b589d280-93a2-449d-bd76-8b7697e81fd9)


![image](https://github.com/user-attachments/assets/cdb48ef1-3129-49a4-8279-bb578d069db7)

Стоит отметить - у данной нейросети странное понимание буйволов

## Локальное развертывание

### 1. Клонируем репозиторий
```shell
git clone https://github.com/Gen1tir0/AnimalRecognition.git
```
### 2. Переходим в директорию скопированного репозитория
```shell
cd AnimalRecognition
```
### 3. Создаем виртуальное окружение в директории и активируем его
```shell
python -m venv .venv
.venv\Scripts\activate 
```
### 4. Устанавливаем зависимости из requirements.txt
```shell
pip install -r requirements.txt
```
### 5. Запускаем backend (uvicorn) и frontend (streamlit)
```shell
uvicorn main:app --host 0.0.0.0 --port 8000
streamlit run app.py
```
### 6. Переходим по ссылке (http://localhost:8501), если нас не перебросило автоматически

## ССЫЛКИ
[Streamlit-приложение](https://animalrecognition-front.onrender.com)\
[FastAPI-приложение](https://animalrecognition-a2sd.onrender.com)

## ПРИМЕР ЗАПРОСА

![image](https://github.com/user-attachments/assets/42e258bf-1991-4bc0-afeb-f5b2dfa3800e)


Отправленное изображение

![1200px-African_Buffalo_(Syncerus_caffer)_cow_ _(50118835268)](https://github.com/user-attachments/assets/766e251b-0890-4bcd-b864-e1ce9b1f764d)



