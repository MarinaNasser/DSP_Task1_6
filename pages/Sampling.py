import streamlit as st
import matplotlib.pyplot as plt
from scipy import signal
from scipy.interpolate import interp1d
import numpy as np  # np mean, np random ,np asarray, np 


def getYCoordinate(newTimeAxisPoint, signalAfterSampling, samplingPeriod):
    summation = 0
    for n in range(0, len(signalAfterSampling)):
        summation = summation + signalAfterSampling[n] * np.sinc((1 / samplingPeriod) * (newTimeAxisPoint - n * samplingPeriod))
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
    analogSignal_time = np.linspace(0, 5, 3000)
    selectedOptionAxis.plot(analogSignal_time, st.session_state['signal'][option])
    selectedOptionAxis.grid()
    st.plotly_chart(selectedOptionFigure)

    samplingFrequency = st.sidebar.slider('Sampling frequency', 1, 100, 2)
    print(samplingFrequency)
    samplingPeriod = 1 / samplingFrequency

    discreteTimeUnnormalised = np.arange(0, 5 / samplingPeriod)
    discreteTime = discreteTimeUnnormalised * samplingPeriod

    predict = interp1d(analogSignal_time, st.session_state['signal'][option], kind='quadratic')
    signalAfterSampling = np.array([predict(t) for t in discreteTime])

    interpolatedSignal, interpolatedAxis = plt.subplots(1, 1)

    reconstructionTimeAxis = np.linspace(0, analogSignal_time[-1], 400)
    signalAfterReconstruction = np.array([getYCoordinate(timePoint, signalAfterSampling, samplingPeriod) for timePoint in reconstructionTimeAxis])

    interpolatedAxis.plot(discreteTime, signalAfterSampling, 'go-', reconstructionTimeAxis, signalAfterReconstruction, '.-')
    st.plotly_chart(interpolatedSignal)
else:
    st.write('Generate signals then choose a one to sample')
