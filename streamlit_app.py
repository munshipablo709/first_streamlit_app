#Tie is apython file

import streamlit  
import pandas
import requests
import snowflake.connector
from urllib.error import URLError


def get_fruityvice_data(this_fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
  return fruityvice_normalized

streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast Menu')
streamlit.text('  🥣 Omega 3 Blueberry oatmeal')
streamlit.text('  🥗  Kale Spinach and Rocket Smoothies')
streamlit.text('  🐔  Hard-boiled Free-range Egg')
streamlit.text(' 🥑🍞 Avocado Toast ')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')


# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

# fruit info picker
streamlit.header("Fruityvice Fruit Advice!")
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  #streamlit.write('The user entered ', fruit_choice)
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information.")
  else:
    back_from_function = get_fruityvice_data(fruit_choice)
    streamlit.dataframe(back_from_function)

except URLError as e:
    streamlit.error()


#new section to display fruityvie advice
#streamlit.text(fruityvice_response.json())
# write your own comment -what does the next line do? 
# write your own comment - what does this do?


streamlit.stop()


# connect to snowflake
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from pc_rivery_db.public.fruit_load_list")
#my_data_row = my_cur.fetchone()
my_data_rows = my_cur.fetchall()
streamlit.text("The fruitload list contains:")
streamlit.dataframe(my_data_rows)



# fruit addition box
add_my_fruit = streamlit.text_input('What fruit would you like to add?','Jackfruit')
streamlit.write('Thanks for adding ', add_my_fruit)

#error test
my_cur.execute("insert into pc_rivery_db.public.fruit_load_list values ('from sreamli')")
