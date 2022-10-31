from pickle import TRUE
import streamlit as st  # data web app development
import matplotlib.pyplot as plt
import numpy as np  # np mean, np random ,np asarray
import pandas as pd
from scipy.interpolate import interp1d
import scipy
from scipy.signal import find_peaks

st.set_page_config(
    page_title="DSP TASK 1",
    page_icon="✅",
    layout = "wide",
    initial_sidebar_state="expanded"
)

column1, column2 = st.columns((4, 1), gap="small")

uploaded_file = st.sidebar.file_uploader("Choose a CSV file 📂 ")

with column2:
    color = st.color_picker('Pick the signal color', '#1f72ab')

if 'noise' not in st.session_state:
    st.session_state['noise'] = False

if 'checkBoxes' not in st.session_state:
    st.session_state['checkBoxes'] = {}

if 'primaryKey' not in st.session_state:
    st.session_state['primaryKey'] = 0

if 'signal' not in st.session_state:
    st.session_state['signal'] = {}

if 'amp_freq' not in st.session_state:
    st.session_state['amp_freq'] = {}

if 'uploaded' not in st.session_state:
    st.session_state['uploaded'] = {}

if 'sum' not in st.session_state:
    st.session_state['sum'] = [np.linspace(0, 5, 3000),np.zeros(3000)]

if 'button_state' not in st.session_state:
    st.session_state['button_state']=True
if 'fMax' not in st.session_state:
    st.session_state['fMax'] = 1

#-----------------------------------------------------------get Fmax----------------------------------------------------------------
def getFMax(xAxis,yAxis):
    amplitude = np.abs(scipy.fft.rfft(yAxis))
    frequency = scipy.fft.rfftfreq(len(xAxis), (xAxis[1]-xAxis[0]))
    indices = find_peaks(amplitude)
    if len(indices[0])>0 :
        max_freq=round(frequency[indices[0][-1]])
    else:
        max_freq=1   
    return max_freq
  


#-----------------------------------------------------------sinc interpolation----------------------------------------------------------------
def getYCoordinate(newPoint, signalAfterSampling, samplingPeriod,discreteTime):
    summation = 0
    for discreteTimePoint,correspondingSignalValue in zip(discreteTime, signalAfterSampling):
        summation = summation + correspondingSignalValue * np.sinc((1 / samplingPeriod) * (newPoint - discreteTimePoint ))
    return summation



#-----------------------------------------------------------sampling----------------------------------------------------------------

def sample(signalX,signalY,originalCheckBox,sampleCheckBox,reconstructionCheckBox,samplingFrequency):

    snr_db = 50
    agree = False
    if uploaded_file is None:
        agree = st.sidebar.checkbox('Noise')

    if agree and uploaded_file is None:
        st.session_state['noise'] = True
        snr_db = st.sidebar.slider('SNR (dB)', 1, 50, 1)  # units
        # signal-to-noise ratio is defined as the ratio of the power of the signal to the power of the noise
        signal_power = st.session_state['sum'][1] ** 2 # calculate signal power
        signal_power_db = 10 * np.log10(signal_power) # convert signal power to db
        signal_average_power = np.mean(signal_power)  # calculate signal average power
        signal_average_power_db = 10 * np.log10(signal_average_power)  # convert signal average power to db
        noise_db = signal_average_power_db - snr_db  # calculate noise in db
        noise_watts = 10 ** (noise_db / 10)  # converts noise from db to watts
        # generate a sample of white noise
        mean_noise = 0
        noise = np.random.normal(mean_noise, np.sqrt(noise_watts), len(st.session_state['sum'][0]))


    else:
        st.session_state['noise'] = False

    
    finalSignalFigure, finalSignalAxis = plt.subplots(1, 1)
    analogSignal_time = signalX
    if st.session_state['noise'] and uploaded_file is None:
        analogSignalValue=signalY+ noise
    else:
        analogSignalValue = signalY
    finalSignalAxis.grid()
    font1 = {'family':'serif','color':'white','size':20}
    plt.xlabel("Time (seconds)",fontdict = font1)
    plt.ylabel("Amplitude",fontdict = font1)

    print(samplingFrequency)
    samplingPeriod = 1 / samplingFrequency
    
    discreteTime = np.arange(analogSignal_time[0],analogSignal_time[-1],samplingPeriod)
    # discreteTime[3] = ana
    
    predict = interp1d(analogSignal_time, analogSignalValue, kind='quadratic')
    signalAfterSampling = np.array([predict(timePoint) for timePoint in discreteTime])

    # reconstructionTimeAxis = np.linspace(analogSignal_time[0], analogSignal_time[-1], 600,endpoint=False)
    #line 63 takes high processing time than 61 because it includes much more points to process
    reconstructionTimeAxis = analogSignal_time
    
    signalAfterReconstruction = np.array([getYCoordinate(timePoint, signalAfterSampling, samplingPeriod,discreteTime) for timePoint in reconstructionTimeAxis])
    
    if originalCheckBox:
        finalSignalAxis.plot(analogSignal_time, analogSignalValue,color=color,linewidth=4)
    if sampleCheckBox:
        finalSignalAxis.plot(discreteTime, signalAfterSampling,'r.',linewidth=3)
    if reconstructionCheckBox:
        finalSignalAxis.plot(reconstructionTimeAxis, signalAfterReconstruction, 'y--',linewidth=3)
    
    
    st.plotly_chart(finalSignalFigure,use_container_width=True)

#-----------------------------------------------------------check boxes----------------------------------------------------------------
with column2:
    original_signal=st.checkbox('Original signal',value = True)
    reconstructed_signal=st.checkbox('Reconstructed signal')
    sampling_point=st.checkbox('Sampling Points')

with column2:
    samplingFrequency = 1
    if reconstructed_signal or sampling_point:
        # initial = getFMax(analogSignal_time,changeableSignal)
        
        samplingFrequency =st.session_state['fMax']* st.slider('Fs/Fmax', 1.0, 10.0, 2.0)

#-----------------------------------------------------------generated signals----------------------------------------------------------------

if uploaded_file is None:
    frequency = st.sidebar.slider('Frequency (Hz)', 1, 20, 1)
    amplitude = st.sidebar.slider('Amplitude', 1, 10, 1)
    
    analogSignal_time = np.linspace(0, 5, 3000) #x-axis
    changeableSignal = amplitude * np.sin(2 * np.pi * frequency * analogSignal_time) #y-axis


    # addressing the selected checkboxes and the other ones
    chosenCheckBoxes = []
    leftCheckBoxes = []
    for index, value in st.session_state['checkBoxes'].items():
        if value:
            chosenCheckBoxes.append(index)
        else:
            leftCheckBoxes.append(index)



    # addition of more than one signal
    if st.sidebar.button('Add Signal'):
        st.session_state['primaryKey'] += 1
        PK = st.session_state['primaryKey']
        st.session_state['signal'][PK] = [analogSignal_time, changeableSignal]
        st.session_state['uploaded'][PK] = False
        st.session_state['sum'][1] = st.session_state['sum'][1] + st.session_state['signal'][PK][1]
        st.session_state['amp_freq'][PK] = [amplitude,frequency]
        st.session_state['fMax'] = getFMax(st.session_state['sum'][0],st.session_state['sum'][1])


    with column1:
        sample(st.session_state['sum'][0],st.session_state['sum'][1],original_signal,sampling_point,reconstructed_signal,samplingFrequency)

    with column2:
        # expander for the generated signals checkboxes
        expander = st.expander('Generated signals')
        atLeastOneAdded = False
        for index, sgnal in st.session_state['signal'].items():
            if st.session_state['uploaded'][index]:
                # st.session_state['checkBoxes'][index] = expander.checkbox('freq {} amp {}',disabled = True)
                continue
            atLeastOneAdded = True
            st.session_state['checkBoxes'][index] = expander.checkbox('{}) Amp={}, Freq={}'.format(index,st.session_state['amp_freq'][index][0],st.session_state['amp_freq'][index][1]))

    
        # deleting the selected signals from the checkboxes and from the st.session_state['signal']
        if atLeastOneAdded:
            if st.button('➖Delete Signal')  :
                for index in chosenCheckBoxes:
                    st.session_state['checkBoxes'].pop(index)
                    st.session_state['sum'][1] -= st.session_state['signal'][index][1]
                    st.session_state['signal'].pop(index)
                    # st.session_state['primaryKey'] -= 1
                st.experimental_rerun()

#-----------------------------------------------------------save file-------------------------------------------------------------------
    with column1:
        if st.button('Save as CSV 📩'):
            data = {'t':st.session_state['sum'][0],'signal':st.session_state['sum'][1]}
            df = pd.DataFrame(data)
            df.set_index('t', inplace=True)
            df.to_csv('Signal {}.csv'.format(st.session_state['primaryKey']))
            st.success("The file has been saved successfully", icon="✅")

#-----------------------------------------------------------uploaded file-------------------------------------------------------------------

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
    list_of_columns=df.columns
    with column1:
        df = df.drop_duplicates(keep = 'first',subset=[list_of_columns[0]])
        analogSignalTime = df[list_of_columns[0]].to_numpy()
        analogSignalValue = df[list_of_columns[1]].to_numpy()

    with column1:
        st.session_state['fMax'] = getFMax(analogSignalTime,analogSignalValue)
        sample(analogSignalTime,analogSignalValue,original_signal,sampling_point,reconstructed_signal,samplingFrequency)
