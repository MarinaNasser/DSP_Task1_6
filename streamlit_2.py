import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from bokeh.layouts import column, row
from bokeh.models import CustomJS, Slider
from bokeh.plotting import ColumnDataSource, figure, show
import random
import time



st.title('DSP')
#st.text('this is a webpage to practice nyquest theory')


upload_file = st.file_uploader('upload your file here')

# Amplitude = st.sidebar.slider('amplitude', 0, 130, 25)

amplitude = st.sidebar.slider('Amplitude', 0.1, 10.0, 1.0)
phase = st.sidebar.slider('Phase', 0, 7, 0)
frequency = st.sidebar.slider('Frequency', 1.0, 100.0, 20.0)
offset = st.sidebar.slider('Offset', -5, 5, 0)
samplingFrequency = st.sidebar.slider('Sampling frequency', 1.0, 1000.0, 50.0)

freq = 20 # Hz
t = np.linspace(0, 0.5, 200)
y1 = offset + amplitude * np.sin(2 * np.pi * frequency * t + phase)

noise=0.0008*np.asarray(random.sample(range(0,1000),200))

if st.sidebar.button('Add noise'):
    y1 = offset + amplitude * np.sin(2 * np.pi * frequency * t + phase)+noise
if st.sidebar.button('Delete noise'):
    y1 = offset + amplitude * np.sin(2 * np.pi * frequency * t + phase)

st.text('Before Sampling')

fig1,ax1 = plt.subplots(1,1)
ax1.plot(t,y1)
plt.grid()
st.pyplot(fig1)



print(samplingFrequency)
T = 1 / samplingFrequency
n = np.arange(0, 0.5 / T)
# print(n)
nT = n * T
# print(nT)
y2 = np.sin(2 * np.pi * frequency * nT) # Since for sampling t = nT.


fig2,ax2 = plt.subplots(1,1)
#ax.plot(nT,y2)
ax2=plt.stem(nT,y2,'m','g-')
st.text('After Sampling')
plt.grid()
st.pyplot(fig2)


