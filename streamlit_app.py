#Tie is apython file

import streamlit  
import pandas

streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast Menu')
streamlit.text('  🥣 Omega 3 Blueberry oatmeal')
streamlit.text('  🥗  Kale Spinach and Rocket Smoothies')
streamlit.text('  🐔  Hard-boiled Free-range Egg')
streamlit.text(' 🥑🍞 Avocado Toast ')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamliut.dataframe(my_fruit_list)
