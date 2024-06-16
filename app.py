import tensorflow as tf
from tensorflow.keras.models import load_model
import streamlit as st
import numpy as np

st.header('Image Classification Model')

# Use a raw string or forward slashes to avoid unicode issues
model_path = r'C:\Users\rokha\Downloads\Fruits_Vegetables\Image_classify.keras'
model = load_model(model_path)

data_cat = [
    'apple', 'banana', 'beetroot', 'bell pepper', 'cabbage', 'capsicum', 
    'carrot', 'cauliflower', 'chilli pepper', 'corn', 'cucumber', 'eggplant', 
    'garlic', 'ginger', 'grapes', 'jalepeno', 'kiwi', 'lemon', 'lettuce', 
    'mango', 'onion', 'orange', 'paprika', 'pear', 'peas', 'pineapple', 
    'pomegranate', 'potato', 'raddish', 'soy beans', 'spinach', 'sweetcorn', 
    'sweetpotato', 'tomato', 'turnip', 'watermelon'
]

img_height = 180
img_width = 180

image = st.text_input('Enter Image name', 'Apple.jpg')

# Ensure the image path is correct
try:
    image_load = tf.keras.utils.load_img(image, target_size=(img_height, img_width))
    img_arr = tf.keras.utils.img_to_array(image_load)
    img_bat = tf.expand_dims(img_arr, 0)

    predict = model.predict(img_bat)
    score = tf.nn.softmax(predict)

    st.image(image, width=200)
    st.write(f'Veg/Fruit in image is {data_cat[np.argmax(score)]}')
    st.write(f'With accuracy of {np.max(score) * 100:.2f}%')
except Exception as e:
    st.write(f"Error loading image: {e}")
