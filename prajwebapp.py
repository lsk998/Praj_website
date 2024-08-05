import streamlit as st
st.set_page_config(page_title="Mywebpage",page_icon=":tada:",layout="wide")
#import requests
#from streamlit_lottie import st_lottie



#Using local cssthis function will tak file name as an argument
      

#header 
st.subheader ("Hi,I am Prajwal :wave:")
st.title("Structural Engineer from India")
st.write("I am passionate about AI and Data Science and Architechture")
st.write("[Learn more LinkedIn>](https://www.linkedin.com/in/prajwal-kapade-b08b201a7/)")

#what are the services I provide
st.write("---")
left_column, right_column =st.columns(2)
with left_column:
    st.header("What exactly I do?")
    st.write("On Youtube I have a channel named Praj where I upload informative videos")
    st.write("[Youtube Channel link>](https://www.youtube.com/@KapadeLalit/videos)")




#CONTACT Details
st.write("---")
st.write("Get in touch with me:wave:")
st.write("[Email>] prajwalkapade@outlook.com")
st.write("Mob:8767349768")

