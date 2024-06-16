# Fruit_veg_image_classification_model

This project demonstrates an end-to-end pipeline for image classification using Convolutional Neural Networks (CNNs) with TensorFlow and an interactive web application built with Streamlit.


## Table of Contents
Overview
Dataset
Model Architecture
Installation
Usage
Results
Technologies Used
Contributing
License
Overview
The goal of this project is to classify images of fruits and vegetables using a deep learning model. The model is trained on a dataset containing various categories of fruits and vegetables and deployed using Streamlit to create an interactive web app for real-time predictions.

## Dataset
The dataset includes images of the following categories:

Apple
Banana
Beetroot
Bell Pepper
Cabbage
Capsicum
Carrot
Cauliflower
Chilli Pepper
Corn
Cucumber
Eggplant
Garlic
Ginger
Grapes
Jalapeno
Kiwi
Lemon
Lettuce
Mango
Onion
Orange
Paprika
Pear
Peas
Pineapple
Pomegranate
Potato
Raddish
Soy Beans
Spinach
Sweetcorn
Sweetpotato
Tomato
Turnip
Watermelon

## Model Architecture
The model is built using a CNN with the following architecture:

Rescaling layer to normalize pixel values
Convolutional layers with ReLU activation and max pooling
Flatten layer to convert 2D features to 1D
Dropout layer to prevent overfitting
Dense layers for classification

## Installation
Clone the repository and install the necessary packages:


git clone https://github.com/your-username/Fruits_Vegetables_Image_Classification.git](https://github.com/ummefahad/Fruit_veg_image_classification_model.git
cd Fruits_Vegetables_Image_Classification
conda create -n streamlit_env python=3.11
conda activate streamlit_env
pip install -r requirements.txt
Usage
Run the Streamlit app:

streamlit run app.py
Results
The model achieves high accuracy in classifying images of fruits and vegetables. Below is a sample output from the Streamlit app:


Technologies Used
Python
TensorFlow
Streamlit
NumPy
Matplotlib
Pandas
## Contributing
Contributions are welcome! Please fork this repository and submit a pull request.

## License
This project is licensed under the MIT License.

