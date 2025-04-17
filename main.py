from fastapi import FastAPI, File
from fastapi.responses import JSONResponse
from keras.models import load_model
import numpy as np

from image_preprocess import image_preprocess

model = load_model("Trained_Resnet.h5", compile=False)
model.save('Trained_Resnet.h5')
labels = {0: 'Buffalo', 1: 'Elephant', 2: 'Rhino', 3: 'Zebra'}

app = FastAPI()


@app.post("/predict/")
async def predict(file: bytes = File()):
    try:
        processed_image = image_preprocess(file)
        model_preds = model.predict(processed_image)[0]
        predicted_class = labels[np.argmax(model_preds)]
        probabilities = {str(label): float(probability)
                         for label, probability in zip(labels.values(), model_preds)}
        return JSONResponse({
            "class": predicted_class,
            "probabilities": probabilities
        })
    except Exception as e:
        return JSONResponse(status_code=200, content={
            "message": "An error has occurred!",
            "error_text": str(e)
        })
