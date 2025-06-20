# tensorflow is a pre-trained machine learning model that can look at an image and classify it
# opencv allows manipulations on the image that we load, so that it can get passed through tensorflow

import cv2
import numpy as np
import streamlit as st
from tensorflow.keras.applications.mobilenet_v2 import (
    MobileNetV2,
    preprocess_input,
    decode_predictions
)
from PIL import Image

