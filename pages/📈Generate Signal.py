import streamlit as st  # data web app development
import matplotlib.pyplot as plt
import numpy as np  # np mean, np random ,np asarray, np 
import pandas as pd

st.set_page_config(
    page_title="DSP TASK 1",
    page_icon="✅",
    layout = "wide",
    initial_sidebar_state="expanded"
)

c1, c2 = st.columns((4, 2),gap="small")


# st.title('Customise your signal')


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

if 'sum' not in st.session_state:
    st.session_state['sum'] = [np.linspace(0, 5, 3000),np.zeros(3000)]

if 'button_state' not in st.session_state:
    st.session_state['button_state']=True
    
#--------------------------------------------------------------------
 
with c2:
    uploaded_file = st.file_uploader("Choose a CSV file 📂 ")


    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        
        list_of_columns=df.columns

        fig, ax = plt.subplots()
        df = df.drop_duplicates(keep = 'first',subset=[list_of_columns[0]])
        analogSignalTime = df[list_of_columns[0]].to_numpy()
        analogSignalValue = df[list_of_columns[1]].to_numpy()
        ax.plot(analogSignalTime,analogSignalValue)
        # st.write(type(analogSignalTime))
        # st.write(type(analogSignalValue))
        
        if 'primaryKey' not in st.session_state:
            st.session_state['primaryKey'] = 0
        if 'signal' not in st.session_state:
            st.session_state['signal'] = {}
        if 'uploaded' not in st.session_state:
            st.session_state['uploaded'] = {}
        
        st.session_state['primaryKey'] = st.session_state['primaryKey'] + 1
        st.session_state['signal'][st.session_state['primaryKey']] = [analogSignalTime,analogSignalValue]
        st.session_state['uploaded'][st.session_state['primaryKey']] = True
        st.plotly_chart(fig,use_container_width=True)
#--------------------------------------------------------------------



#sliders
with c2:
    color = st.color_picker('Pick the signal color', '#00f900')
amplitude = st.sidebar.slider('Amplitude', 1, 10, 1)
frequency = st.sidebar.slider('Frequency (Hz)', 1, 20, 1)
snr_db = st.sidebar.slider('SNR (dB)', 1.0, 50.0, 1.0)  # units
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

agree = st.sidebar.checkbox('Noise')

if agree:
    st.session_state['noise'] = True
else:
    st.session_state['noise'] = False


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

# add noise or do not
if st.session_state['noise']:
    changeableSignal = amplitude * np.sin(2 * np.pi * frequency * analogSignal_time) + noise
else:
    changeableSignal = amplitude * np.sin(2 * np.pi * frequency * analogSignal_time)
   


# addressing the selected checkboxes and the other ones
chosenCheckBoxes = []
leftCheckBoxes = []
for index, value in st.session_state['checkBoxes'].items():
    if value:
        chosenCheckBoxes.append(index)
    else:
        leftCheckBoxes.append(index)



# addition of more than one signal
if st.sidebar.button('✖️ Add Signal'):
    st.session_state['primaryKey'] = st.session_state['primaryKey'] + 1
    st.session_state['signal'][st.session_state['primaryKey']] = [analogSignal_time, changeableSignal]
    st.session_state['uploaded'][st.session_state['primaryKey']] = False
    st.session_state['sum'][1] = st.session_state['sum'][1] + st.session_state['signal'][st.session_state['primaryKey']][1]




# deleting the selected signals from the checkboxes and from the st.session_state['signal']
if st.sidebar.button('➖Delete Signal'):
    for index in chosenCheckBoxes:
        st.session_state['checkBoxes'].pop(index)
        st.session_state['sum'][1] -= st.session_state['signal'][index][1]
        st.session_state['signal'].pop(index)

with c1:
    # showing the signal according to the changes of the sidebar sliders
    changeableSignalFigure, changeableSignalAxis = plt.subplots(1, 1)
    changeableSignalAxis.plot(st.session_state['sum'][0], st.session_state['sum'][1],color=color, linewidth=3)
    changeableSignalAxis.grid()
    st.plotly_chart(changeableSignalFigure,  linewidth=3)

with c2:
    original_signal=st.checkbox('Original signal')
    reconstructed_signal=st.checkbox('Reconstructed signal')
    sampling_point=st.checkbox('Sampling Points')

with c2:
    
# expander for the generated signals checkboxes
    expander = st.expander('Generated signals')
    for index, sgnal in st.session_state['signal'].items():
        if st.session_state['uploaded'][index]:
            st.session_state['checkBoxes'][index] = expander.checkbox('signal {}'.format(index),disabled = True)
            continue
        st.session_state['checkBoxes'][index] = expander.checkbox('signal {}'.format(index))


# viewing the generated signals
# for index, sgnal in st.session_state['signal'].items():
#     if st.session_state['checkBoxes'][index]:
#         st.write('Signal {}'.format(index))
#         signalFigure, signalAxis = plt.subplots(1, 1)
#         signalAxis.plot(sgnal[0], sgnal[1], linewidth=3)
#         signalAxis.grid()
#         st.plotly_chart(signalFigure, linewidth=3,use_container_width=True)



#--------------------------------------------------------------------
#save file
if st.button('Save as CSV 📩'):
    if len(st.session_state['signal'] )==0:
      st.warning('No signal is generated', icon="⚠️")
    elif len(chosenCheckBoxes)==0:
        st.warning('Check the required signal', icon="⚠️")
    else:
        for checkBoxIndex in chosenCheckBoxes:
            data = {'t':st.session_state['signal'][checkBoxIndex][0],
                    'signal':st.session_state['signal'][checkBoxIndex][1]}
            df = pd.DataFrame(data)
            df.set_index('t', inplace=True)
            df.to_csv('Signal {}.csv'.format(checkBoxIndex))
            st.success("The file has been saved successfully", icon="✅")

