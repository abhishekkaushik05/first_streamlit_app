import streamlit as st
import pandas as pd
import requests

st.title('My Parents New Healthy Diner')

st.header('Breakfast Favorites')
st.text('🥣 Omega 3 and Bluberry Oatmeal')
st.text('🥗 Kale, Spinach and Rocket Smoothie')
st.text('🐔 Hard-Boiled Free-Range Egg')
st.text('🥑🍞 Avocado Toast')
st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list= my_fruit_list.set_index('Fruit')
fruits_selected=st.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

st.dataframe(fruits_to_show)

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "kiwi")
# st.text(fruityvice_response.json()) removed this raw json line

st.header("Fruityvice Fruit Advice!")
# json data is converted into table using pandas 
fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
# display the tabular data on screen
st.dataframe(fruityvice_normalized)

fruit_choice = st.text_input('What fruit would you like information about?','Kiwi')
st.write('The user entered ', fruit_choice)
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
