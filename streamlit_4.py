import streamlit as st 
# imported streamlit 
st.title("taking input from user")
#we are going to some of input types of streamlit 
roll =st.input_int("enter your roll-number",min =1,max=100)

#in above step we have taken the input as integer as roll-number
name =st.input_text("Enter your name :")
#now we have taken the input as a string 
dob =st.date_input("Enter your date of birth ")
#we have taken date by usin date_input ()
time=st.time_input("current time: ")
#st.time_input() used to take time 
about=st.text_ara("Enter in which domain you intested ")
# text_area() used to take a long string
current-date-time= st.datetime_input("select")
#it usally used to know current time-date
file = st.file_uploader("upload")
#used to upload the files
capture =st.camera_input("capture a pic  ")
# it usally uses your camera to camture pic
record= st.audio_input("RECORD")
#for taking the audio
pick=st.color_picker()
#picking a color 
chat=st.chat_input()
#taking chat as input
rating = st.feedback()
#to take feedback from the user
edit =st.data_editor()
# to edit the tables 
st.write(f"your roll-number is {roll} \n your name is {name} \n your date of birth is {dob} \n about : {about} \n applied on   {current-date-time} \n  uploaded documents {file} \n captured pic :{capture} \n color picked : {pick} \n rating : {rating} ")
#to display the data collected
