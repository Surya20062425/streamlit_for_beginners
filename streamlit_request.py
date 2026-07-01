import streamlit as st
#imported streamlit
import requests
# imported requests
st.tite("reuests")
st.number_input("enter currency")
target_currency=st.selectbox("select currency",["usd","inr","eur"])
# created a selectbox to take the cuurency type
if st.button("cover"):
  url ="url"
  #use a working url
  response =requests.get(url)
  #geting response from the url

   if response.status_code ==200:
     data =response.json()
     #storing the  response in json format
     rate =data["rate"][target_currency]
     #targeting to convert the currency type
     convert=rate *120
     #converting the currency
     st.success(f"{target_curency} is {convert} usd ")
     pass

else : 
   st.error("invalid url")
