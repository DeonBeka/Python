import pandas as pd
import streamlit as st
import plotly.express as px

books_df = pd.read_csv

st.title("Bestselling Books Analysis")
st.write("This app analyzes the Amazon Top Selling Books from 2009 to 2022")

st.sidebar.header("Add New Book data")
with st.sidebar.form("book_form"):
    new_name = st.text_input("Book Name")
    new_author = st.text_input("Author")
    new_user_rating = st.slider("User Rating", 0.0 , 5.0, 0.0, 0.1)
    new_reviews = st.number_input("Reviews", min_value= 0, step=1)
    new_price = st.number_input("Price", min_value= 0, step=1)
    new_year = st.number_input("Year", min_value= 2009, max_value=2022, step= 1)
    new_genre = st.selectbox("Genre", books_df['Genre'].unique())
    submit_button = st.form_submit_button(label="Add Book")