import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.title('DSP')
st.text('this is a webpage to practice nyquest theory')

upload_file = st.file_uploader('upload your file here')

Amplitude = st.sidebar.slider('Amplitude', 0, 130, 25)
Frequency = st.slider('Frequency', 0.1, 1000.0, 25.0)

f = 20 # Hz
t = np.linspace(0, 0.5, 200)
x1 = np.sin(2 * np.pi * f * t)

s_rate = Frequency # Hz. Here the sampling frequency is less than the requirement of sampling theorem

print(s_rate)
T = 1 / s_rate
n = np.arange(0, 0.5 / T)
# print(n)
nT = n * T
# print(nT)
x2 = np.sin(2 * np.pi * f * nT) # Since for sampling t = nT.


fig,ax = plt.subplots(1,1)
ax.plot(nT,x2)
st.pyplot(fig)

# plt.figure(figsize=(10, 8))
# plt.suptitle("Sampling a Sine Wave of Fmax=20Hz with fs=50Hz", fontsize=20)

# plt.subplot(2, 2, 1)
# plt.plot(t, x1, linewidth=3, label='SineWave of frequency 20 Hz')
# plt.xlabel('time.', fontsize=15)
# plt.ylabel('Amplitude', fontsize=15)
# plt.legend(fontsize=10, loc='upper right')

# plt.subplot(2, 2, 2)
# plt.plot(nT, x2, 'ro', label='Sample marks after resampling at fs=50Hz')
# plt.xlabel('time.', fontsize=15)
# plt.ylabel('Amplitude', fontsize=15)
# plt.legend(fontsize=10, loc='upper right')

# plt.subplot(2, 2, 3)
# plt.stem(nT, x2, 'm', label='Sample after resampling at fs=50Hz')
# plt.xlabel('time.', fontsize=15)
# plt.ylabel('Amplitude', fontsize=15)
# plt.legend(fontsize=10, loc='upper right')

# plt.subplot(2, 2, 4)
# plt.plot(nT, x2, 'g-', label='Reconstructed Sine Wave')
# plt.xlabel('time.', fontsize=15)
# plt.ylabel('Amplitude', fontsize=15)
# plt.legend(fontsize=10, loc='upper right')

# plt.tight_layout()

# st.pyplot(plt.figure())

# if upload_file:
#     df = pd.read_csv(upload_file)
#     st.write(df.describe())