import streamlit as st # data web app development
import matplotlib.pyplot as plt
import numpy as np  # np mean, np random ,np asarray, np 
import pandas as pd  # read csv, df manipulation
from bokeh.layouts import column, row
from bokeh.models import CustomJS, Slider
from bokeh.plotting import ColumnDataSource, figure, show
import random

#import plotly.express as px  # interactive charts

st.set_page_config(
    page_title="DSP TASK 1",
    page_icon="✅",

)

st.title('DSP')