import streamlit as st
import pandas

st.set_page_config(layout="wide")

st.title("The Best Company")

co_info = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
"""
st.write(co_info)

st.subheader("Our Team")

col1, col2, col3 = st.columns([1,1,1])

df = pandas.read_csv("data.csv")

#Iterate over first 4 rows in data.csv
with col1:
    for index, row in df[:4].iterrows():
        st.header(f'{row["first name"].title()} {row["last name"].title()}')
        st.subheader(row["role"])
        st.image("images/" + row["image"])
  
#Iterate over middle 4 rows in data.csv      
with col2:
    for index, row in df[4:8].iterrows():
        st.header(f'{row["first name"].title()} {row["last name"].title()}')
        st.subheader(row["role"])
        st.image("images/" + row["image"])
        
#Iterate over last 4 rows in data.csv
with col3:
    for index, row in df[8:12].iterrows():
        st.header(f'{row["first name"].title()} {row["last name"].title()}')
        st.subheader(row["role"])
        st.image("images/" + row["image"])