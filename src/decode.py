import numpy as np
import base64
import cv2


def dec(baseImg):
    img_binary = base64.b64decode(baseImg)
    jpg = np.frombuffer(img_binary, dtype=np.uint8)
    img = cv2.imdecode(jpg, cv2.IMREAD_COLOR)
    return img
