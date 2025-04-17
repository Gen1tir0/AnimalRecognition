import cv2
from io import BytesIO
import numpy as np
from PIL import Image


def image_preprocess(byte_image):
    image = np.asarray(Image.open(BytesIO(byte_image)))
    resized = cv2.resize(image, (64, 64))
    expanded = np.reshape(resized, (1, 64, 64, 3))
    print(expanded.shape)
    return expanded
