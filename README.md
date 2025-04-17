# 4-class Animal Recognition
## Что это за проект? ##
Учебный проект, представляющий собой систему для классификации животных - *носорог, буйвол, зебра, слон* с использованием модели глубокого обучения на основе ResNet50. Именно эта модель показала себя лучше всего по итогам сравнения\
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
**Anaconda**
### 1. Клонируем репозиторий
```shell
git clone https://github.com/Gen1tir0/AnimalRecognition.git
```
### 2. Скачиваем файл с обученной моделью с Google-диска: [(тык)](https://drive.google.com/file/d/1cj29PP584LGyIaY0LZDxTwCX-pL9amht/view?usp=sharing) и помещаем его в папку проекта. Модель, используемая в данном проекте, не пропускается из-за размера
### 3. Создаем виртуальное окружение и активируем его
```shell
conda create --n my_venv python=3.10
conda activate my_venv
```
### 4. Устанавливаем зависимости из requirements.txt
```shell
conda install --file requirements.txt
```
### 5. Запускаем backend (uvicorn) и frontend (streamlit)
```shell
uvicorn main:app --host 0.0.0.0 --port 8000
streamlit run app.py
```
### 6. Переходим по ссылке (http://localhost:8501), если нас не перебросило автоматически

## ССЫЛКИ
[Streamlit-приложение](https://animalrecognition-front.onrender.com)
[FastAPI-приложение](https://animalrecognition-a2sd.onrender.com)

## ПРИМЕР ЗАПРОСА

![image](https://github.com/user-attachments/assets/7ab50883-23e3-40e6-96aa-c255adb2bf8a)
![image](https://github.com/user-attachments/assets/bba03ce3-523a-4dd2-91f9-e665a730609e)
