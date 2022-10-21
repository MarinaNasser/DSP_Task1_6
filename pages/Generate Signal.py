import streamlit as st  # data web app development
import matplotlib.pyplot as plt
import numpy as np  # np mean, np random ,np asarray, np 

st.set_page_config(layout="wide")

st.sidebar.markdown("Generating signals")

if 'noise' not in st.session_state:
    st.session_state['noise'] = False

if 'checkBoxes' not in st.session_state:
    st.session_state['checkBoxes'] = {}

if 'primaryKey' not in st.session_state:
    st.session_state['primaryKey'] = 0

if 'signal' not in st.session_state:
    st.session_state['signal'] = {}

amplitude = st.sidebar.slider('Amplitude', 1, 10, 1)
frequency = st.sidebar.slider('Frequency', 1, 20, 1)
snr_db = st.sidebar.slider('SNR', 1.0, 50.0, 1.0)  # units

analogSignal_time = np.linspace(0, 5, 3000)

changeableSignal = amplitude * np.sin(2 * np.pi * frequency * analogSignal_time)

power = changeableSignal ** 2
signal_power_db = 10 * np.log10(power)
signal_average_power = np.mean(power)  # calculate signal power
signal_average_power_db = 10 * np.log10(signal_average_power)  # convert signal power to db
noise_db = signal_average_power_db - snr_db  # calculate noise
noise_watts = 10 ** (noise_db / 10)  # converts noise from db to watts

# generate a sample of white noise
mean_noise = 0
noise = np.random.normal(mean_noise, np.sqrt(noise_watts), len(changeableSignal))

if st.sidebar.button('Add noise'):
    st.session_state['noise'] = True

if st.sidebar.button('Delete noise'):
    st.session_state['noise'] = False

# add noise or do not
if st.session_state['noise']:
    changeableSignal = amplitude * np.sin(2 * np.pi * frequency * analogSignal_time) + noise
else:
    changeableSignal = amplitude * np.sin(2 * np.pi * frequency * analogSignal_time)

# generate button
if st.sidebar.button('Generate'):
    st.session_state['primaryKey'] = st.session_state['primaryKey'] + 1
    st.session_state['signal'][st.session_state['primaryKey']] = [analogSignal_time, changeableSignal]

# addressing the selected checkboxes and the other ones
chosenCheckBoxes = []
leftCheckBoxes = []
for index, value in st.session_state['checkBoxes'].items():
    if value:
        chosenCheckBoxes.append(index)
    else:
        leftCheckBoxes.append(index)

# deleting the selected signals from the checkboxes and from the st.session_state['signal']
if st.sidebar.button('delete'):
    for index in chosenCheckBoxes:
        st.session_state['checkBoxes'].pop(index)
        st.session_state['signal'].pop(index)

st.text('Before Sampling')

# showing the signal according the changes of the sidebar sliders
changeableSignalFigure, changeableSignalAxis = plt.subplots(1, 1)
changeableSignalAxis.plot(analogSignal_time, changeableSignal, color='red', linewidth=5)
changeableSignalAxis.grid()
st.plotly_chart(changeableSignalFigure)

# addition of more than one signal
if st.sidebar.button('add'):
    summedSignal = np.zeros(3000)
    atLeastOneChecked = False

    for checkBoxIndex in chosenCheckBoxes:
        atLeastOneChecked = True
        summedSignal = summedSignal + st.session_state['signal'][checkBoxIndex][1]

    # if there is anything to plot
    if atLeastOneChecked:
        st.session_state['primaryKey'] = st.session_state['primaryKey'] + 1
        st.session_state['signal'][st.session_state['primaryKey']] = [analogSignal_time, summedSignal]

# expander for the generated signals checkboxes
expander = st.expander('Generated signals')
for index, sgnal in st.session_state['signal'].items():
    st.session_state['checkBoxes'][index] = expander.checkbox('signal {}'.format(index))

# viewing the generated signals
for index, sgnal in st.session_state['signal'].items():
    if st.session_state['checkBoxes'][index]:
        st.write('Signal {}'.format(index))
        signalFigure, signalAxis = plt.subplots(1, 1)
        signalAxis.plot(sgnal[0], sgnal[1])
        signalAxis.grid()
        st.plotly_chart(signalFigure)
