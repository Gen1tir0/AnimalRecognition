import streamlit as st
import requests
from PIL import Image
from io import BytesIO
from streamlit_drawable_canvas import st_canvas

URL = "http://127.0.0.1:8000/predict/"


def get_prediction(image_data):
    try:
        response = requests.post(
            URL,
            files={"file": ("image.png", image_data, "image/png")}
        )
        response.raise_for_status()
        data = response.json()
        return str(data["class"]), ''.join('{} - {}%\n'.format(key, round(val*100, 3)) for key, val in data["probabilities"].items())
    except requests.exceptions.RequestException as e:
        st.error(f"Ошибка при отправке запроса: {e}")
    except ValueError as e:
        st.error(f"Ошибка при обработке ответа: {e}")
    return None


def preprocess_image_client(image):
    if image.mode == 'RGBA':
        image = image.convert('RGB')
    elif image.mode == 'L':
        image = image.convert('RGB')

    # Изменяем размер до 28x28
    image = image.resize((224, 224))
    img_byte_arr = BytesIO()
    image.save(img_byte_arr, format="PNG")
    img_byte_arr = img_byte_arr.getvalue()

    return img_byte_arr


st.title("Невероятная классификация изображений")

mode = st.radio("Режим ввода", ["Загрузить", "Нарисовать"])

if mode == "Загрузить":
    file = st.file_uploader("Загрузка изображений", type=["jpg", "jpeg", "png"])
    if file:
        col1, col2 = st.columns(2)

        with col1:
            original_image = Image.open(file).convert("RGB")
            st.image(original_image, caption="Загруженное изображение")

        prepared_image = preprocess_image_client(original_image)
        prediction, probabilities = get_prediction(prepared_image)
        if prediction is not None:
            with col2:
                st.text(f"Нейросеть думает, что это {prediction}")
                st.text(f"Вероятности:\n{probabilities}")

elif mode == "Нарисовать":
    stroke_width = st.slider("Толщина линии:", 1, 25, 9)

    col_color1, col_color2 = st.columns(2)
    with col_color1:
        stroke_color = st.color_picker("Цвет линии:", "#FFFFFF")
    with col_color2:
        bg_color = st.color_picker("Цвет фона:", "#000000")

    realtime_update = st.checkbox("Обновлять в реальном времени", True)

    col1, col2 = st.columns(2)

    with col1:
        canvas_result = st_canvas(
            fill_color="rgba(0, 0, 0, 0)",
            stroke_width=stroke_width,
            stroke_color=stroke_color,
            background_color=bg_color,
            update_streamlit=realtime_update,
            height=280,
            width=280,
            drawing_mode="freedraw",
            key="canvas",
        )

    if canvas_result.image_data is not None:
        original_image = Image.fromarray(canvas_result.image_data.astype('uint8'), 'RGB')
        prepared_image = preprocess_image_client(original_image)
        prediction, probabilities = get_prediction(prepared_image)
        if prediction is not None:
            with col2:
                st.text(f"Нейросеть думает, что это {prediction}")
                st.text(f"Вероятности:\n{probabilities}")
