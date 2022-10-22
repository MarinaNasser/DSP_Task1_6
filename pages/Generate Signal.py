from sqlalchemy import true
import streamlit as st  # data web app development
import matplotlib.pyplot as plt
import numpy as np  # np mean, np random ,np asarray, np 
import pandas as pd

st.set_page_config(layout="wide")


if 'noise' not in st.session_state:
    st.session_state['noise'] = False

if 'checkBoxes' not in st.session_state:
    st.session_state['checkBoxes'] = {}

if 'primaryKey' not in st.session_state:
    st.session_state['primaryKey'] = 0

if 'signal' not in st.session_state:
    st.session_state['signal'] = {}

if 'uploaded' not in st.session_state:
    st.session_state['uploaded'] = {}


#sliders

amplitude = st.sidebar.slider('Amplitude', 1, 10, 1)
frequency = st.sidebar.slider('Frequency', 1, 20, 1)
snr_db = st.sidebar.slider('SNR', 1.0, 50.0, 1.0)  # units
#--------------------------------------------------------------------

analogSignal_time = np.linspace(0, 5, 3000) #x-axis

changeableSignal = amplitude * np.sin(2 * np.pi * frequency * analogSignal_time) #y-axis

#--------------------------------------------------------------------

#measuring noise

# signal-to-noise ratio is defined as the ratio of the power of the signal to the power of the noise
signal_power = changeableSignal ** 2 # calculate signal power
signal_power_db = 10 * np.log10(signal_power) # convert signal power to db
signal_average_power = np.mean(signal_power)  # calculate signal average power
signal_average_power_db = 10 * np.log10(signal_average_power)  # convert signal average power to db
noise_db = signal_average_power_db - snr_db  # calculate noise in db
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


#--------------------------------------------------------------------


# generate button
if st.sidebar.button('Generate Signal'):
    st.session_state['primaryKey'] = st.session_state['primaryKey'] + 1
    st.session_state['signal'][st.session_state['primaryKey']] = [analogSignal_time, changeableSignal]
    st.session_state['uploaded'][st.session_state['primaryKey']] = False;
    


# addressing the selected checkboxes and the other ones
chosenCheckBoxes = []
leftCheckBoxes = []
for index, value in st.session_state['checkBoxes'].items():
    if value:
        chosenCheckBoxes.append(index)
    else:
        leftCheckBoxes.append(index)


# deleting the selected signals from the checkboxes and from the st.session_state['signal']
if st.sidebar.button('Delete Signal'):
    for index in chosenCheckBoxes:
        st.session_state['checkBoxes'].pop(index)
        st.session_state['signal'].pop(index)



# showing the signal according to the changes of the sidebar sliders
changeableSignalFigure, changeableSignalAxis = plt.subplots(1, 1)
changeableSignalAxis.plot(analogSignal_time, changeableSignal, color='red', linewidth=3)
changeableSignalAxis.grid()
st.plotly_chart(changeableSignalFigure, linewidth=3)


# addition of more than one signal
if st.sidebar.button('Add signal'):
    summedSignal = np.zeros(3000)
    atLeastOneChecked = False

    for checkBoxIndex in chosenCheckBoxes:
        atLeastOneChecked = True
        summedSignal = summedSignal + st.session_state['signal'][checkBoxIndex][1]

    # if there is anything to plot
    if atLeastOneChecked:
        st.session_state['primaryKey'] = st.session_state['primaryKey'] + 1
        st.session_state['signal'][st.session_state['primaryKey']] = [analogSignal_time, summedSignal]
        st.session_state['uploaded'][st.session_state['primaryKey']] = False


# expander for the generated signals checkboxes
expander = st.expander('Generated signals')
for index, sgnal in st.session_state['signal'].items():
    if st.session_state['uploaded'][index]:
        st.session_state['checkBoxes'][index] = expander.checkbox('signal {}'.format(index),disabled = True)
        continue
    st.session_state['checkBoxes'][index] = expander.checkbox('signal {}'.format(index))

# viewing the generated signals
for index, sgnal in st.session_state['signal'].items():
    if st.session_state['checkBoxes'][index]:
        st.write('Signal {}'.format(index))
        signalFigure, signalAxis = plt.subplots(1, 1)
        signalAxis.plot(sgnal[0], sgnal[1], linewidth=3)
        signalAxis.grid()
        st.plotly_chart(signalFigure, linewidth=3)

#--------------------------------------------------------------------
#save file
if st.button('Save'):
    if len(st.session_state['signal'] )==0:
      st.warning('No signal is generated', icon="⚠️")
    elif len(chosenCheckBoxes)==0:
        st.warning('Check the required signal', icon="⚠️")
    else:
        for checkBoxIndex in chosenCheckBoxes:
            data = st.session_state['signal'][checkBoxIndex][1]
            df = pd.DataFrame(data)
            df.to_csv('Signal {}.csv'.format(index))
            st.success("The file has been saved successfully", icon="✅")

