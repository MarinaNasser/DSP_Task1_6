import streamlit as st
import matplotlib.pyplot as plt
from scipy import signal
import numpy as np  # np mean, np random ,np asarray, np 

def getTheYCoordinates(newX,signalX,signalY):
    print('------------------------------')
    y = []
    for x_coordinate in newX:
        for index in range(0,len(signalX)):
            if x_coordinate < signalX[index]:
                previousXIndex = index-1
                followingXIndex = index
                break
        followingX = signalX[followingXIndex]
        previousX = signalX[previousXIndex]
        followingY = signalY[followingXIndex]
        previousY = signalY[previousXIndex]
        newYCoordinate = (x_coordinate-followingX)*(previousY - followingY)/(previousX - followingX)+(followingY)
        y.append(newYCoordinate)
    
    return y        

def signaltonoise(a, axis=0, ddof=0):
    a = np.asanyarray(a)
    m = a.mean(axis)
    sd = a.std(axis=axis, ddof=ddof)
    return np.where(sd == 0, 0, m/sd)

option = 0
if 'signal' in st.session_state:
    signals = []
    for index,sgnal in st.session_state['signal'].items():
        signals.append('Signal {}'.format(index))
    option = st.selectbox('Choose a signal to sample',signals)
if option != 0:
    option = int(option[7:])
    fig,ax = plt.subplots(1,1)
    t = np.linspace(0, 5, 3000)
    ax.plot(t,st.session_state['signal'][option])
    ax.grid()
    st.plotly_chart(fig)
    
    
    frequency = 2
    samplingFrequency = st.sidebar.slider('Sampling frequency', 1.0, 100.0, 2.0)
    print(samplingFrequency)
    T = 1 / samplingFrequency
    n = np.arange(0, 5 / T)
    nT = n * T
    # y2 = np.sin(2 * np.pi * frequency * nT) # Since for sampling t = nT.
    y2 = getTheYCoordinates(nT,t,st.session_state['signal'][option])
     
    fig2,ax2 = plt.subplots(1,1)

    f = signal.resample(y2, 200)
    xnew = np.linspace(0, 5, 200, endpoint=False)
    ax2.plot(nT, y2, 'go-', xnew, f, '.-')
    st.plotly_chart(fig2)
else:
    st.write('Generate signals then choose a one to sample')
