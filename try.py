import streamlit as st
import numpy as np
Amplitude = st.sidebar.slider('Amplitude', 0, 130, 25)
Frequency = st.slider('Frequency', 0, 130, 25)
def sin_wave_signal(Amplitude,Phase,signalFrequency,samplingFrequency):
    samplingPeriod=1/samplingFrequency
    NumOfsamples=int(samplingFrequency/signalFrequency)                   #number of samples
    x_axis=np.linspace(0,(NumOfsamples-1)*samplingPeriod , NumOfsamples) #time steps
    y_axis=Amplitude
    np.sin(2np.pisignalFrequency*x_axis+Phase)