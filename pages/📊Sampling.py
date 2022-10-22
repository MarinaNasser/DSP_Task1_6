import streamlit as st
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
import numpy as np  # np mean, np random ,np asarray, np 

col1, col2, col3 = st.columns(3)
with col2:
    st.title('Sampling')

def getYCoordinate(newTimeAxisPoint, signalAfterSampling, samplingPeriod,discreteTime):
    summation = 0
    for x,y in zip(discreteTime, signalAfterSampling):
        summation = summation + y * np.sinc((1 / samplingPeriod) * (newTimeAxisPoint - x ))
    print(summation)
    return summation


def signaltonoise(a, axis=0, ddof=0):
    a = np.asanyarray(a)
    m = a.mean(axis)
    sd = a.std(axis=axis, ddof=ddof)
    return np.where(sd == 0, 0, m / sd)


option = 0
if 'signal' in st.session_state:
    signals = []
    for index, sgnal in st.session_state['signal'].items():
        signals.append('Signal {}'.format(index))
    option = st.selectbox('Choose a signal to sample', signals)

if option:

    # get the index of the signal from the chosen string
    option = int(option[7:])

    selectedOptionFigure, selectedOptionAxis = plt.subplots(1, 1)
    analogSignal_time = st.session_state['signal'][option][0]
    analogSignalValue = st.session_state['signal'][option][1]
    
    selectedOptionAxis.plot(analogSignal_time, analogSignalValue)
    selectedOptionAxis.grid()
    # st.plotly_chart(selectedOptionFigure)

    samplingFrequency = st.sidebar.slider('Sampling frequency', 1, 100, 2)
    print(samplingFrequency)
    samplingPeriod = 1 / samplingFrequency
    discreteTimeUnNormalised = np.arange(analogSignal_time[0]/samplingPeriod, analogSignal_time[-1] / samplingPeriod)
    discreteTime = discreteTimeUnNormalised * samplingPeriod
    
    predict = interp1d(analogSignal_time, analogSignalValue, kind='quadratic')
    signalAfterSampling = np.array([predict(timePoint) for timePoint in discreteTime])

    interpolatedSignalFigure, interpolatedSignalAxis = plt.subplots(1, 1)

    # reconstructionTimeAxis = np.linspace(analogSignal_time[0], analogSignal_time[-1], 200,endpoint=False)
    reconstructionTimeAxis = analogSignal_time

    signalAfterReconstruction = np.array([getYCoordinate(timePoint, signalAfterSampling, samplingPeriod,discreteTime) for timePoint in reconstructionTimeAxis])
    selectedOptionAxis.plot(discreteTime, signalAfterSampling,'r.',reconstructionTimeAxis, signalAfterReconstruction, 'y--')
    st.plotly_chart(selectedOptionFigure)
    

    interpolatedSignalAxis.plot(reconstructionTimeAxis, signalAfterReconstruction, '-')

    st.plotly_chart(interpolatedSignalFigure)
    # st.write(signalAfterReconstruction)

else:
    st.write('Generate signals then choose one to sample')
