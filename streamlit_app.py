import pandas
import streamlit
fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
fruit_list = fruit_list.set_index('Fruit')

selected = streamlit.multiselect("Pick a fruit:", list(fruit_list.index)['Avocado','Strawberries'])
show_selected = fruit_list.loc[selected]

streamlit.dataframe(show_selected)
