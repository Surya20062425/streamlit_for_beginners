import streamlit as st 
# imported the streamlit 
st.title("select-box")
st.write("select one programming language among them :")
# we use selectbox() to select the option
st.selectbox("programming-languages",["java","python","html","css","react.js"])
