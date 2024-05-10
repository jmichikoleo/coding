#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import pandas as pd


# In[ ]:


df = pd.read_csv("bookdatabase.csv")


# In[ ]:


def sidebar_filters(df):
    st.sidebar.title("Filters")
    language = st.sidebar.selectbox("Choose Language", df['Language'].unique())
    trope = st.sidebar.selectbox("Choose Trope", df['Trope'].unique())
    book_type = st.sidebar.selectbox("Choose Book Type", df['Book_Type'].unique())
    return language, trope, book_type

def main_content(df, language, trope, book_type):
    st.title("Library Dashboard")
    
    filtered_df = df[(df['Language'] == language) & 
                     (df['Trope'] == trope) & 
                     (df['Book_Type'] == book_type)]
    
    if len(filtered_df) == 0:
        st.warning("No books found with selected filters.")
    else:
        st.write(filtered_df)

def main():
    st.set_page_config(page_title="Library Dashboard")
    st.title("Welcome to the Library Dashboard")

    df = pd.read_csv("bookdatabase.csv")

    language, trope, book_type = sidebar_filters(df)

    main_content(df, language, trope, book_type)

if __name__ == "__main__":
    main()

