import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from bokeh.layouts import column, row
from bokeh.models import CustomJS, Slider
from bokeh.plotting import ColumnDataSource, figure, show
from scipy import signal



st.title('DSP')
st.text('this is a webpage to practice nyquest theory')

upload_file = st.file_uploader('upload your file here')

Amplitude = st.sidebar.slider('amplitude', 0, 130, 25)

amplitude = st.slider('Amplitude', 0.1, 10.0, 1.0)
phase = st.slider('Phase', 0, 7, 0)
frequency = st.slider('Frequency', 1.0, 20.0, 2.0)
offset = st.slider('Offset', -5, 5, 0)

f = 20 # Hz
t = np.linspace(0, 5, 3000)
y1 = offset + amplitude * np.sin(2 * np.pi * frequency * t + phase)


fig1,ax1 = plt.subplots(1,1)
ax1.plot(t,y1)
ax1.grid()
ax1.set_xticks(np.arange(1,5))
ax1.set_xticks(np.arange(1,5))
st.pyplot(fig1)

samplingFrequency = st.slider('Sampling frequency', 1.0, 40.0, 2.0)

print(samplingFrequency)
T = 1 / samplingFrequency
n = np.arange(0, 5 / T)
# print(n)
nT = n * T
# print(nT)
y2 = offset + amplitude * np.sin(2 * np.pi * frequency * nT + phase) # Since for sampling t = nT.




fig,ax = plt.subplots(1,1)
ax.plot(nT,y2)

# x = np.linspace(0, 10, 200, endpoint=False)
# y = np.cos(-x**2/6.0)
f = signal.resample(y2, 200)
xnew = np.linspace(0, 5, 200, endpoint=False)
# import matplotlib.pyplot as plt
ax.plot(nT, y2, 'go-', xnew, f, '.-')
# ax.legend(['data', 'resampled'], loc='best')

# plt.show()


st.plotly_chart(fig)

