from distutils.command.upload import upload
from sqlalchemy import false
import streamlit as st
from collections import deque
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd
from matplotlib.animation import FuncAnimation 



uploaded_file = st.file_uploader("Choose a CSV file")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    # st.dataframe(df)
    # st.write(df)

    list_of_columns=df.columns

    fig, ax = plt.subplots()
    df = df.drop_duplicates(keep = 'first',subset=[list_of_columns[0]])
    analogSignalTime = df[list_of_columns[0]].to_numpy()
    analogSignalValue = df[list_of_columns[1]].to_numpy()
    ax.plot(analogSignalTime,analogSignalValue)
    st.write(type(analogSignalTime))
    st.write(type(analogSignalValue))
    
    if 'primaryKey' not in st.session_state:
        st.session_state['primaryKey'] = 0
    if 'signal' not in st.session_state:
        st.session_state['signal'] = {}
    if 'uploaded' not in st.session_state:
        st.session_state['uploaded'] = {}
    
    st.session_state['primaryKey'] = st.session_state['primaryKey'] + 1
    st.session_state['signal'][st.session_state['primaryKey']] = [analogSignalTime,analogSignalValue]
    st.session_state['uploaded'][st.session_state['primaryKey']] = True
    st.plotly_chart(fig)

