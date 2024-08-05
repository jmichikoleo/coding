#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import streamlit as st
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder

data = [
    {'food_name': 'Rice', 'total_carbs': 45, 'fiber': 1, 'protein': 4, 'fat': 0.5, 'glycemic_index': 73, 'pre_meal_blood_sugar': 100, 'post_meal_blood_sugar': 180},
    {'food_name': 'Bread', 'total_carbs': 75, 'fiber': 3, 'protein': 8, 'fat': 1, 'glycemic_index': 70, 'pre_meal_blood_sugar': 100, 'post_meal_blood_sugar': 160},
    {'food_name': 'Mie Ayam','total_carbs': 50, 'fiber': 2, 'protein': 10, 'fat': 7, 'glycemic_index': 60, 'pre_meal_blood_sugar': 100, 'post_meal_blood_sugar': 145},
    {'food_name': 'Mie Babi', 'total_carbs': 55, 'fiber': 2, 'protein': 12, 'fat': 8, 'glycemic_index': 65, 'pre_meal_blood_sugar': 100, 'post_meal_blood_sugar': 160},
    {'food_name': 'Nasi Uduk', 'total_carbs': 45, 'fiber': 2, 'protein': 4, 'fat': 5, 'glycemic_index': 70, 'pre_meal_blood_sugar': 100, 'post_meal_blood_sugar': 165},
    {'food_name': 'Nasi Padang', 'total_carbs': 50, 'fiber': 3, 'protein': 6, 'fat': 10, 'glycemic_index': 75, 'pre_meal_blood_sugar': 100,'post_meal_blood_sugar': 165},
    {'food_name': 'Cereal', 'total_carbs': 60, 'fiber': 5, 'protein': 5, 'fat': 2, 'glycemic_index': 80, 'pre_meal_blood_sugar': 100, 'post_meal_blood_sugar': 170},
    {'food_name': 'Oatmeal', 'total_carbs': 55, 'fiber': 8, 'protein': 6, 'fat': 3, 'glycemic_index': 55, 'pre_meal_blood_sugar': 100, 'post_meal_blood_sugar': 120},
    {'food_name': 'Ayam Goreng', 'total_carbs': 10, 'fiber': 0, 'protein': 15, 'fat': 8, 'glycemic_index': 45, 'pre_meal_blood_sugar': 85, 'post_meal_blood_sugar': 115},
    {'food_name': 'Babi Panggang', 'total_carbs': 5, 'fiber': 0, 'protein': 20, 'fat': 15, 'glycemic_index': 50, 'pre_meal_blood_sugar': 90, 'post_meal_blood_sugar': 120},
    {'food_name': 'Cumi Goreng Tepung', 'total_carbs': 30, 'fiber': 1, 'protein': 10, 'fat': 10, 'glycemic_index': 65, 'pre_meal_blood_sugar': 95, 'post_meal_blood_sugar': 140},
    {'food_name': 'Ayam Geprek', 'total_carbs': 15, 'fiber': 1, 'protein': 18, 'fat': 12, 'glycemic_index': 50, 'pre_meal_blood_sugar': 90, 'post_meal_blood_sugar': 125},
    {'food_name': 'Sate Kambing', 'total_carbs': 5, 'fiber': 0, 'protein': 25, 'fat': 20, 'glycemic_index': 50, 'pre_meal_blood_sugar': 85, 'post_meal_blood_sugar': 115},
    {'food_name': 'Sate Padang', 'total_carbs': 25, 'fiber': 1, 'protein': 15, 'fat': 10, 'glycemic_index': 60, 'pre_meal_blood_sugar': 90, 'post_meal_blood_sugar': 130},
    {'food_name': 'Sop Kambing', 'total_carbs': 20, 'fiber': 2, 'protein': 20, 'fat': 15, 'glycemic_index': 55, 'pre_meal_blood_sugar': 85, 'post_meal_blood_sugar': 120},
    {'food_name': 'Bakso', 'total_carbs': 25, 'fiber': 1, 'protein': 12, 'fat': 8, 'glycemic_index': 60, 'pre_meal_blood_sugar': 90, 'post_meal_blood_sugar': 135}
]

df = pd.DataFrame(data)

# Preprocessing
encoder = OneHotEncoder(sparse_output=False)  # Adjust this line based on your scikit-learn version
encoded_foods = encoder.fit_transform(df[['food_name']])
encoded_foods_df = pd.DataFrame(encoded_foods, columns=encoder.get_feature_names_out(['food_name']))
df = pd.concat([df, encoded_foods_df], axis=1)
df.drop(['food_name'], axis=1, inplace=True)

# Train the model
X = df.drop('post_meal_blood_sugar', axis=1)
y = df['post_meal_blood_sugar']
model = LinearRegression()
model.fit(X, y)

# Streamlit app
st.title("Blood Sugar Predictor")

# Input: Pre-meal blood sugar
pre_meal_blood_sugar = st.number_input("Enter your blood sugar level before eating:", min_value=0)

# Input: Food selection
food_options = list(encoder.categories_[0])
selected_food = st.selectbox("Choose your food:", food_options)

# Nutritional information (this should ideally come from your dataset)
nutritional_info = {
    'Rice': {'total_carbs': 45, 'fiber': 1, 'protein': 4, 'fat': 0.5, 'glycemic_index': 73},
    'Bread': {'total_carbs': 75, 'fiber': 3, 'protein': 8, 'fat': 1, 'glycemic_index': 70},
    'Noodle': {'total_carbs': 55, 'fiber': 2, 'protein': 6, 'fat': 1, 'glycemic_index': 50},
    # Add more nutritional info...
}

if st.button("Predict"):
    # Get selected food's nutritional values
    food_nutrition = nutritional_info[selected_food]
    
    # Create input for prediction
    input_data = {
        'total_carbs': food_nutrition['total_carbs'],
        'fiber': food_nutrition['fiber'],
        'protein': food_nutrition['protein'],
        'fat': food_nutrition['fat'],
        'glycemic_index': food_nutrition['glycemic_index'],
        'pre_meal_blood_sugar': pre_meal_blood_sugar
    }
    
    # Create DataFrame for prediction
    input_df = pd.DataFrame([input_data])
    
    # One-hot encode the food
    encoded_input = encoder.transform([[selected_food]])
    encoded_input_df = pd.DataFrame(encoded_input, columns=encoder.get_feature_names_out(['food_name']))
    input_df = pd.concat([input_df, encoded_input_df], axis=1)
    
    # Ensure the order of columns matches the model training
    input_df = input_df[X.columns]  # Align with training features
    
    # Make prediction
    predicted_blood_sugar = model.predict(input_df)
    
    # Display prediction
    st.write(f"Predicted post-meal blood sugar: {predicted_blood_sugar[0]:.2f}")

