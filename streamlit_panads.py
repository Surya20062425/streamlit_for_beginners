import streamlit as st
# importes streamlit
import pandas as pd 
# imported pandas
st.title("pandas")
file =st.file_uploader("insert file:",type ="csv")
if file :
  pd.read_csv(file)
  # to read the csv file
  st.subheader(file)
  df=  st.dataframe((file)
  # it displays the data in a format

if file :
  st.subheader("summary :")
  st.write(df.describe())
  # it actually summarise the data

if file :
  filter =df["attribute"].unique()
  # select the data we want to filter 
  selector =st.selectbox("select",attribute)
  data =df[df["attribute"]==selecter]
  # gathers the data we needed
  st.dataframe(data)
  # displays the data in  format
  
