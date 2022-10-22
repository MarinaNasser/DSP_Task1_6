import streamlit as st # data web app development


st.set_page_config(
    page_title="DSP TASK 1",
    page_icon="✅",
)

col1, col2, col3 = st.columns(3)
with col2:
    st.title('DSP Task 1')
 
st.header('Welcome to our Sampling Studio')
st.write('In this studio you can generate your own signal, add 2 or more signals together, delete an added signal, do sampling, save your signal in an csv file, and finally you can do all on an uploaded signal of your choice.')