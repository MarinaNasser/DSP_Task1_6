import numpy as np
from scipy import signal,fft,fftpack
x = np.linspace(0, 10, 20, endpoint=False)
y = np.cos(-x**2/6.0)
f = signal.resample(y, 100)
xnew = np.linspace(0, 10, 400, endpoint=False)
import matplotlib.pyplot as plt
plt.plot(x, y, 'go-', xnew, f, '.-', 10, y[0], 'ro')
plt.legend(['data', 'resampled'], loc='best')
plt.show()

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

import numpy as np
import matplotlib.pyplot as plt
f1=300
fs=800
t_min =0
t_max= 10/f1
t= np.arange(t_min,t_max,.00001)
x1=np.sin(2*np.pi*f1*t)
Ts= 1/fs
ts = np.arange(t_min,t_max,Ts)
x1resampled=np.sin(2*np.pi*f1*ts)
x1reconstructed=np.zeros(len(t))
samples = len(ts)
for i in range(1,len(t)):
    for n in range(1,samples):
        x1reconstructed[i]=x1reconstructed[i]+x1resampled[n]*np.sinc((t[i]-n*Ts)/Ts);
plt.subplot(3,1,1)
plt.plot(t,x1)

plt.subplot(3,1,2)
plt.scatter(ts,x1resampled)


plt.subplot(3,1,3)
plt.plot(t,x1reconstructed)
plt.show()

# viewing the generated signals
# for index, sgnal in st.session_state['signal'].items():
#     if st.session_state['checkBoxes'][index]:
#         st.write('Signal {}'.format(index))
#         signalFigure, signalAxis = plt.subplots(1, 1)
#         signalAxis.plot(sgnal[0], sgnal[1], linewidth=3)
#         signalAxis.grid()
#         st.plotly_chart(signalFigure, linewidth=3,use_container_width=True)

## change state every click
# if st.sidebar.button('Noise'):
#     if st.session_state['button_state']==True:
#         st.session_state['noise'] = True
#         st.session_state['button_state']=False
#     else:
#         st.session_state['noise'] = False
#         st.session_state['button_state']=True

# if st.sidebar.button('➖Delete noise'):
#     st.session_state['noise'] = False
# showing the summation of signals
# changeableSignalFigure, changeableSignalAxis = plt.subplots(1, 1)
# changeableSignalAxis.plot(st.session_state['sum'][0], st.session_state['sum'][1],color=color, linewidth=3)
# changeableSignalAxis.grid()
# st.plotly_chart(changeableSignalFigure,  linewidth=3)

#---------------------------------------------------------------- sampling -------------------------------------------------------#

# import streamlit as st
# import matplotlib.pyplot as plt
# from scipy.interpolate import interp1d
# import numpy as np  # np mean, np random ,np asarray, np 

# col1, col2, col3 = st.columns(3)
# with col2:
#     st.title('Sampling')

# def getYCoordinate(newPoint, signalAfterSampling, samplingPeriod,discreteTime):
#     summation = 0
#     for discreteTimePoint,correspondingSignalValue in zip(discreteTime, signalAfterSampling):
#         summation = summation + correspondingSignalValue * np.sinc((1 / samplingPeriod) * (newPoint - discreteTimePoint ))
#     return summation

# option = 0
# if 'signal' in st.session_state:
#     signals = []
#     for index, sgnal in st.session_state['signal'].items():
#         signals.append('Signal {}'.format(index))
#     option = st.selectbox('Choose a signal to sample', signals)

# if option:

#     # get the index of the signal from the chosen string
#     option = int(option[7:])

#     selectedOptionFigure, selectedOptionAxis = plt.subplots(1, 1)
#     analogSignal_time = st.session_state['signal'][option][0]
#     analogSignalValue = st.session_state['signal'][option][1]
    
#     selectedOptionAxis.plot(analogSignal_time, analogSignalValue)
#     selectedOptionAxis.grid()
#     # st.plotly_chart(selectedOptionFigure)

#     samplingFrequency = st.sidebar.slider('Sampling frequency (Hz)', 1, 100, 2)
#     print(samplingFrequency)
#     samplingPeriod = 1 / samplingFrequency
    
#     #the equivalent to line 53
#     # discreteTimeUnNormalised = np.arange(analogSignal_time[0]/samplingPeriod, analogSignal_time[-1] / samplingPeriod)
#     # discreteTime = discreteTimeUnNormalised * samplingPeriod
    
#     #the equivalent to the lines 49 and 50
#     discreteTime = np.arange(analogSignal_time[0],analogSignal_time[-1],samplingPeriod)
    
    
#     predict = interp1d(analogSignal_time, analogSignalValue, kind='quadratic')
#     signalAfterSampling = np.array([predict(timePoint) for timePoint in discreteTime])

#     interpolatedSignalFigure, interpolatedSignalAxis = plt.subplots(1, 1)

#     # reconstructionTimeAxis = np.linspace(analogSignal_time[0], analogSignal_time[-1], 200,endpoint=False)
#     #line 63 takes high processing time than 61 because it includes much more points to process
#     reconstructionTimeAxis = analogSignal_time

#     signalAfterReconstruction = np.array([getYCoordinate(timePoint, signalAfterSampling, samplingPeriod,discreteTime) for timePoint in reconstructionTimeAxis])
#     selectedOptionAxis.plot(discreteTime, signalAfterSampling,'r.',reconstructionTimeAxis, signalAfterReconstruction, 'y--')
    
#     col1, col2 = st.columns(2)
#     with col1:
#         st.plotly_chart(selectedOptionFigure,use_container_width=True)
    

#     interpolatedSignalAxis.plot(reconstructionTimeAxis, signalAfterReconstruction, '-')
#     with col2:
#         st.plotly_chart(interpolatedSignalFigure,use_container_width=True)
#     # st.write(signalAfterReconstruction)

# else:
#     st.write('Generate signals then choose one to sample')


#-------------------------------------------- sampling----------------------------------------------------------------------#

    # st.write(type(analogSignalTime))
    # st.write(type(analogSignalValue))
    
    # if 'primaryKey' not in st.session_state:
    #     st.session_state['primaryKey'] = 0
    # if 'signal' not in st.session_state:
    #     st.session_state['signal'] = {}
    # if 'uploaded' not in st.session_state:
    #     st.session_state['uploaded'] = {}
    
    # st.session_state['primaryKey'] = st.session_state['primaryKey'] + 1
    # st.session_state['signal'][st.session_state['primaryKey']] = [analogSignalTime,analogSignalValue]
    # st.session_state['uploaded'][st.session_state['primaryKey']] = True
    
import scipy

amplitude = np.abs(scipy.fft.rfft(total_signals))
frequency = scipy.fft.rfftfreq(len(initial_time), (initial_time[1]-initial_time[0]))
indices = find_peaks(amplitude)
if len(indices[0])>0 :
    max_freq=round(frequency[indices[0][-1]])
else:
    max_freq=1   


