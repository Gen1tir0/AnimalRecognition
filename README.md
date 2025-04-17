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

|                            |   accuracy |   recall |   precision |       f1 |
|:---------------------------|-----------:|---------:|------------:|---------:|
| Trained ResNet (Work 5)    |      0.981 |    0.981 |    0.98128  | 0.980946 |
| BN&D (Work 4)              |      0.958 |    0.958 |    0.9583   | 0.957958 |
| VGG-like (Work 3)          |      0.868 |    0.868 |    0.869198 | 0.867643 |
| Less stupid (Work 3 - own) |      0.857 |    0.857 |    0.859455 | 0.857496 |
| Stupid (Work 2)            |      0.584 |    0.584 |    0.581787 | 0.578806 |

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



