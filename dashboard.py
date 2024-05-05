#!/usr/bin/env python
# coding: utf-8

# In[5]:


import streamlit as st
import pandas as pd
import os 
import matplotlib.pyplot as plt


# In[3]:


folder_path = os.path.join(os.path.expanduser("~"), "Desktop", "monstermart")
print("Folder path:", folder_path)


# In[4]:


df1 = pd.read_csv('/Users/jleo/Desktop/monstermart/AKULAKU_FEB.csv')


# In[12]:


def generate_pie_chart(file_path):
    df1 = pd.read_csv('/Users/jleo/Desktop/monstermart/AKULAKU_FEB.csv')
    df['Sales'] = pd.to_numeric(df['Sales'], errors='coerce')
    df = df.dropna(subset=['Sales'])
    top_sales = df.groupby('Product')['Sales'].sum().nlargest(10)
    fig, ax = plt.subplots()
    ax.pie(top_sales, labels=top_sales.index, autopct='%1.1f%%', startangle=90)
    ax.axis('equal') 
    st.pyplot(fig)


# In[13]:


def generate_pie_chart(df):
    df['Sales'] = pd.to_numeric(df['Sales'], errors='coerce')
    df = df.dropna(subset=['Sales'])
    top_sales = df.groupby('Product')['Sales'].sum().nlargest(10)
    fig, ax = plt.subplots()
    ax.pie(top_sales, labels=top_sales.index, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')
    st.pyplot(fig)

folder_path = os.path.join(os.path.expanduser("~"), "Desktop", "monstermart")
csv_files = [file for file in os.listdir(folder_path) if file.endswith('.csv')]
selected_file = st.selectbox("Select a CSV file", csv_files)

if selected_file:
    file_path = os.path.join(folder_path, selected_file)
    df = pd.read_csv(file_path)
    st.write(df.head())
    generate_pie_chart(df)


# In[ ]:




