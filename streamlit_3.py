import streamlit as st
#imported streamlit
st.title("st.success")
# we casually use it  to display our select-box in an elegant way
 result = ("res" ,["","pass","fail"])
if res=="" :
  pass

elif res=="pass" :
  st.success("you have been passed the exam")

else :
  st.write("sorry you failed try again !")
