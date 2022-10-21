from distutils.command.upload import upload
from sqlalchemy import false
import streamlit as st
from collections import deque
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd
from matplotlib.animation import FuncAnimation 



uploaded_file = st.file_uploader("Choose a CSV file")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    # st.dataframe(df)
    # st.write(df)

    list_of_columns=df.columns

    fig, ax = plt.subplots()
    # fig.set_animated()
    ax.plot(df[list_of_columns[0]],df[list_of_columns[1]])
    st.plotly_chart(fig)





#el code el adeem ely shaa8al 


# max_samples = 100
# max_x = max_samples
# max_rand = 100

# x = np.arange(0, max_x)
# y = deque(np.zeros(max_samples), max_samples)

# ax.set_ylim(0, max_rand)
# line, = ax.plot(x, np.array(y))
# the_plot = st.pyplot(plt)


# def animate():  # update the y values (every 1000ms)
#     line.set_ydata(np.array(y))
#     the_plot.pyplot(plt)
#     y.append(y) #append y with a random integer between 0 to 100

# for i in range(200):
#     animate()
#     time.sleep(0.01)