import streamlit as st
import numpy as np  # np mean, np random ,np asarray, np 


def signaltonoise(a, axis=0, ddof=0):
    a = np.asanyarray(a)
    m = a.mean(axis)
    sd = a.std(axis=axis, ddof=ddof)
    return np.where(sd == 0, 0, m/sd)

#upload_file = st.file_uploader('upload your file here')

# Amplitude = st.sidebar.slider('amplitude', 0, 130, 25)

amplitude = st.sidebar.slider('Amplitude', 1.0, 10.0, 1.0)
phase = st.sidebar.slider('Phase', 0, 7, 0)
frequency = st.sidebar.slider('Frequency', 1.0, 20.0, 1.0)
offset = st.sidebar.slider('Offset', -5, 5, 0)
samplingFrequency = st.sidebar.slider('Sampling frequency', 1.0, 100.0, 2.0)

# print(samplingFrequency)
# T = 1 / samplingFrequency
# n = np.arange(0, 5 / T)
# # print(n)
# nT = n * T
# # print(nT)
# y2 = np.sin(2 * np.pi * frequency * nT) # Since for sampling t = nT.


# fig2,ax2 = plt.subplots(1,1)
# #ax.plot(nT,y2)
# # ax2=plt.stem(nT,y2,'m','g-')
# f = signal.resample(y2, 200)
# xnew = np.linspace(0, 5, 200, endpoint=False)
# # import matplotlib.pyplot as plt
# ax2.plot(nT, y2, 'go-', xnew, f, '.-')
# # ax.legend(['data', 'resampled'], loc='best')

# # plt.show()


# st.plotly_chart(fig2)
# # ax2=plt.stem(nT,y2,'m','g-')
# # st.text('After Sampling')
# # plt.grid()
# # st.plotly_chart(fig2)
