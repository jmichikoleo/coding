#!/usr/bin/env python
# coding: utf-8

# In[2]:


pip install streamlit


# In[16]:


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


# In[17]:


def load_data():
    data = pd.read_csv('By Product Report From 2024-02-01 To 2024-02-29 For All Machines.csv') 
    return data

data = load_data()
data_filtered = data[['Product', 'Qty Sold']]


# In[18]:


print(data_filtered)


# In[23]:


st.title('Product Sales Feb 2024')
selected_product = st.selectbox('Select a Product', data_filtered['Product'].unique())
product_data = data_filtered[data_filtered['Product'] == selected_product]

st.subheader('Sales Data for Selected Product')
st.write(product_data)

fig, ax = plt.subplots()
ax.bar(product_data['Product'], product_data['Qty Sold'])
ax.set_xlabel('Product')
ax.set_ylabel('Quantity Sold')
ax.set_title('Product Sales')
st.pyplot(fig)

