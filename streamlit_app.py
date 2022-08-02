import pandas
import streamlit
fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(fruit_list)

streamlit.multiselect("Pick a fruit:", list(fruit_list.index))

streamlit.dataframe(fruit_list)
