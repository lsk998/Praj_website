import streamlit as st
st.write("Tool Image Recognition App")

examplelist=['Image_Shiva','Text_Gajanan','Speech_Gita',];
Type=st.selectbox(label="Type",options = examplelist)

passthrough=st.checkbox(
    label="I am a student",
    value=False
)


#predict button
Output=st.button=(label="Show Result")

if Output:
    inputdata={}




url="https://developer.chrome.com/docs/chromedriver/downloads#chromedriver_1140573590/predict"
result=request.post(url,json=inputdata)