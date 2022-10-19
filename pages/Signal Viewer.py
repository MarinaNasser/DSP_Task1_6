from distutils.command.upload import upload
from sqlalchemy import false
import streamlit as st
from collections import deque
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd
from matplotlib.animation import FuncAnimation 


st.sidebar.markdown("Signal Viewer")


#msh sha8aaaaal

# # initializing a figure in 
# # which the graph will be plotted
# fig = plt.figure() 
   
# # marking the x-axis and y-axis
# axis = plt.axes(xlim =(0, 4), 
#                 ylim =(-2, 2)) 
  
# # initializing a line variable
# line, = axis.plot([], [], lw = 3) 
   
# # data which the line will 
# # contain (x, y)
# def init(): 
#     line.set_data([], [])
#     return line,
   
# def animate(i):
#     x = np.linspace(0, 4, 1000)
   
#     # plots a sine graph
#     y = np.sin(2 * np.pi * (x - 0.01 * i))
#     line.set_data(x, y)
      
#     return line,
   
# anim = FuncAnimation(fig, animate, init_func = init,
#                      frames = 200, interval = 20, blit = True)
  
   
# # anim.save('Signal Viewer.mp4', 
# #           writer = 'ffmpeg', fps = 30)










#msh sha8aaaal

# plt.style.use('seaborn-pastel')

#  fig = plt.figure()
# ax = plt.axes(xlim=(0, 4), ylim=(-2, 2))
# line, = ax.plot([], [], lw=3)

# def init():
#     line.set_data([], [])
#     return line,
# def animate(i):
#     x = np.linspace(0, 4, 1000)
#     y = np.sin(2 * np.pi * (x - 0.01 * i))
#     line.set_data(x, y)
#     return line,

# anim = FuncAnimation(fig, animate, init_func=init,
#                                frames=200, interval=20, blit=True)


# anim.save('sine_wave.gif', writer='imagemagick')















#habaaaaal

# uploaded_files = st.file_uploader("Choose a CSV file")

# def get_data() -> pd.DataFrame:
#     return df = pd.read_csv(uploaded_file)


# df = get_data()

#nehayet el habaaaaaal



#msh sha8aal 


# # def upload_file():
# if uploaded_file is not None:
#     df = pd.read_csv(uploaded_file)
#     st.dataframe(df)
#     # st.write(df)

#     list_of_columns=df.columns

#     fig, ax = plt.subplots()
#     fig.set_animated()
#     ax.plot(df[list_of_columns[0]],df[list_of_columns[1]])
#     st.plotly_chart(fig)




















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