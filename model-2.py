#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import streamlit as st
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder

data = [
    {'food_name': 'Rice', 'total_carbs': 45, 'fiber': 1, 'protein': 4, 'fat': 0.5, 'glycemic_index': 73, 'pre_meal_blood_sugar': 120, 'post_meal_blood_sugar': 180},
    {'food_name': 'Bread', 'total_carbs': 75, 'fiber': 3, 'protein': 8, 'fat': 1, 'glycemic_index': 70, 'pre_meal_blood_sugar': 110, 'post_meal_blood_sugar': 160},
    {'food_name': 'Noodle', 'total_carbs': 55, 'fiber': 2, 'protein': 6, 'fat': 1, 'glycemic_index': 50, 'pre_meal_blood_sugar': 100, 'post_meal_blood_sugar': 150},
]

df = pd.DataFrame(data)

encoder = OneHotEncoder(sparse=False)
encoded_foods = encoder.fit_transform(df[['food_name']])
encoded_foods_df = pd.DataFrame(encoded_foods, columns=encoder.get_feature_names_out(['food_name']))
df = pd.concat([df, encoded_foods_df], axis=1)
df.drop(['food_name', 'pre_meal_blood_sugar', 'post_meal_blood_sugar'], axis=1, inplace=True)

X = df.drop('post_meal_blood_sugar', axis=1)
y = df['post_meal_blood_sugar']
model = LinearRegression()
model.fit(X, y)

st.title("Blood Sugar Predictor")

pre_meal_blood_sugar = st.number_input("Enter your blood sugar level before eating:", min_value=0)

food_options = df.columns[df.columns.str.startswith('food_name')]
selected_food = st.selectbox("Choose your food:", food_options)

nutritional_info = {
    'Rice': {'total_carbs': 45, 'fiber': 1, 'protein': 4, 'fat': 0.5, 'glycemic_index': 73},
    'Bread': {'total_carbs': 75, 'fiber': 3, 'protein': 8, 'fat': 1, 'glycemic_index': 70},
    'Noodle': {'total_carbs': 55, 'fiber': 2, 'protein': 6, 'fat': 1, 'glycemic_index': 50},
}

if st.button("Predict"):
    food_nutrition = nutritional_info[selected_food]
    
    input_data = {
        'total_carbs': food_nutrition['total_carbs'],
        'fiber': food_nutrition['fiber'],
        'protein': food_nutrition['protein'],
        'fat': food_nutrition['fat'],
        'glycemic_index': food_nutrition['glycemic_index'],
        'pre_meal_blood_sugar': pre_meal_blood_sugar
    }
    
    input_df = pd.DataFrame([input_data])
    
    encoded_input = encoder.transform([[selected_food]])
    input_df = pd.concat([input_df, pd.DataFrame(encoded_input, columns=encoder.get_feature_names_out(['food_name']))], axis=1)
    
    
    input_df = input_df[X.columns]  
    
    predicted_blood_sugar = model.predict(input_df)
    
    st.write(f"Predicted post-meal blood sugar: {predicted_blood_sugar[0]:.2f}")

