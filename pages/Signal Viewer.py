import streamlit as st
from collections import deque
import matplotlib.pyplot as plt
import numpy as np 
import time  # to simulate a real time data, time loop

st.sidebar.markdown("Signal Viewer")


fig, ax = plt.subplots()

max_samples = 100
max_x = max_samples
max_rand = 100

x = np.arange(0, max_x)
y = deque(np.zeros(max_samples), max_samples)

ax.set_ylim(0, max_rand)
line, = ax.plot(x, np.array(y))
the_plot = st.pyplot(plt)

def animate():  # update the y values (every 1000ms)
    line.set_ydata(np.array(y))
    the_plot.pyplot(plt)
    y.append(np.random.randint(max_x)) #append y with a random integer between 0 to 100

for i in range(200):
    animate()
    time.sleep(0.01)