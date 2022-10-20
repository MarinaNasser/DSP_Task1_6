from cgi import print_form
from msilib.schema import CheckBox
from turtle import width
import streamlit as st # data web app development
import matplotlib.pyplot as plt
import numpy as np  # np mean, np random ,np asarray, np 
import pandas as pd  # read csv, df manipulation
# from bokeh.layouts import column, row
from bokeh.models import  Slider
from bokeh.plotting import ColumnDataSource, figure, show
import random
from scipy import signal
st.sidebar.markdown("Generating signals")

if 'checkBoxes' not in st.session_state:
    st.session_state['checkBoxes'] = {}

if 'primaryKey' not in st.session_state:
    st.session_state['primaryKey'] = 0


if 'signal' not in st.session_state:
    st.session_state['signal'] = {}



amplitude = st.sidebar.slider('Amplitude', 1.0, 10.0, 1.0)
phase = st.sidebar.slider('Phase', 0, 7, 0)
frequency = st.sidebar.slider('Frequency', 1.0, 20.0, 1.0)
offset = st.sidebar.slider('Offset', -5, 5, 0)
snr_db = st.sidebar.slider('SNR', 1.0, 50.0, 1.0) #units



freq = 20 # Hz
t = np.linspace(0, 5, 3000)


signal = offset + amplitude * np.sin(2 * np.pi * frequency * t + phase)
power=signal**2
signal_power_db=10*np.log10(power)
signal_average_power=np.mean(power) #calculate signal power
signal_average_power_db=10*np.log10(signal_average_power) #convert signal power to db
noise_db=signal_average_power_db - snr_db #calculate noise
noise_watts=10**(noise_db/10) #converts noise from db to watts
#generate a sample of white noise 
mean_noise=0
noise=np.random.normal(mean_noise, np.sqrt(noise_watts), len(signal))


#noise=0.0002*np.asarray(random.sample(range(0,3000),3000))

if st.sidebar.button('Add noise'):
    signal = offset + amplitude * np.sin(2 * np.pi * frequency * t + phase)+noise
if st.sidebar.button('Delete noise'):
    signal = offset + amplitude * np.sin(2 * np.pi * frequency * t + phase)
if st.sidebar.button('Generate'):
    st.session_state['primaryKey'] = st.session_state['primaryKey'] + 1
    signal = offset + amplitude * np.sin(2 * np.pi * frequency * t + phase)
    st.session_state['signal'][st.session_state['primaryKey']] = signal


chosenCheckBoxes = []
leftCheckBoxes = []
for index,value in st.session_state['checkBoxes'].items():
    if value == True:
        chosenCheckBoxes.append(index)
    else:
        leftCheckBoxes.append(index)


if st.sidebar.button('delete'):
    for index in chosenCheckBoxes:
        st.session_state['checkBoxes'].pop(index)
        st.session_state['signal'].pop(index)

for index,sgnal in st.session_state['signal'].items():
    st.session_state['checkBoxes'][index] = st.sidebar.checkbox('signal {}'.format(index))

st.text('Before Sampling')



fig1,ax1 = plt.subplots(1,1)
ax1.plot(t,signal, color='red',linewidth=5)
ax1.grid()
st.plotly_chart(fig1)



st.write('Generated signals')
for index,sgnal in st.session_state['signal'].items():
    st.write('Signal {}'.format(index))
    fig,ax = plt.subplots(1,1)
    ax.plot(t,sgnal , color='red',linewidth=5)
    ax.grid()
    st.plotly_chart(fig)

st.write(st.session_state['signal'])




if st.sidebar.button('add'):
    sum = np.zeros(3000)
    atLeastOneChecked = False
    
    for checkBoxIndex in chosenCheckBoxes:
        atLeastOneChecked = True
        for index,sgnal in st.session_state['signal'].items():
            if(index == checkBoxIndex):
                sum = sum + sgnal
                    
    # if there is anything to plot
    if atLeastOneChecked:
        fig1,ax1 = plt.subplots(1,1)
        ax1.plot(t,sum)
        ax1.grid()
        st.plotly_chart(fig1)
