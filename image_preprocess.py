import cv2
from io import BytesIO
import numpy as np
from PIL import Image


def image_preprocess(byte_image):
    image = np.asarray(Image.open(BytesIO(byte_image)))
    image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    resized = cv2.resize(image, (64, 64))
    expanded = np.reshape(resized, (1, 64, 64, 1))
    print(expanded.shape)
    return expanded
