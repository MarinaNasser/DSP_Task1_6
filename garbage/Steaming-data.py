from bokeh.io import curdoc
from bokeh.models import ColumnDataSource, DatetimeTickFormatter, Select ,RangeSlider , CustomJS , Slider
from bokeh.layouts import layout, column , row
from bokeh.plotting import figure , curdoc ,  output_file , show
from bokeh.driving import linear
from datetime import datetime
from math import radians
import numpy as np
import pandas as pd


# def create_value():
#     draw= np.random.randint(0,2, size=200)
#     steps= np.where(draw>0,1,-1)
#     walk= steps.cumsum() #[-1,1]
#     return walk[-1]

# source= ColumnDataSource(dict(x=[],y=[]))
# p=figure(x_axis_type="datetime", width=1500, height=400)
# p.circle(x="x", y="y", color="red" , line_color="red", source=source)
# p.line(x="x", y="y", source=source , line_width=3, line_alpha=0.5)

# x = np.linspace(0, 10, 500)
# y = np.sin(x)


df=pd.read_csv(r"C:\Users\Marina\Downloads\EMG_Healthy_Modified_Less_Data.csv")
x = df['Time']
y = df['Value']


source = ColumnDataSource(data=dict(x=x, y=y))

plot = figure(y_range=(-10, 10), width=1000, height=500)

plot.line('x', 'y', source=source, line_width=3, line_alpha=0.6)

amp_slider = Slider(start=0.1, end=10, value=1, step=.1, title="(-) Amplitude (+)")
phase_slider = Slider(start=0, end=6.4, value=0, step=.1, title="(-) Phase (+)")
freq_slider = Slider(start=0.1, end=50, value=1, step=.1, title="(-) Frequency (+)")
sampling_frequency_slider = Slider(start=0.1, end=50, value=0, step=.1, title="(-) Sampling Frequency (+)")



callback = CustomJS(args=dict(source=source, amp=amp_slider, freq=freq_slider, phase=phase_slider, samp=sampling_frequency_slider),
                    code="""
    const data = source.data;
    const A = amp.value;
    const k = freq.value;
    const phi = phase.value;
    const B = samp.value;
    const x = data['x']
    const y = data['y']
    for (let i = 0; i < x.length; i++) {
        y[i] = B + A*Math.sin(k*x[i]+phi);
    }
    source.change.emit();
""")

amp_slider.js_on_change('value', callback)
freq_slider.js_on_change('value', callback)
phase_slider.js_on_change('value', callback)
sampling_frequency_slider.js_on_change('value', callback)

layout = row(
    plot,
    column(amp_slider, freq_slider, phase_slider, sampling_frequency_slider),
)

show(layout)


#Create Periodic Function
# def update():
#     new_data=dict(x=[datetime.now()], y=[create_value()])
#     source.stream(new_data, rollover=200)
#     p.title.text="Streaming %s Data" % select.value


#Callback function
# def update_intermed(attrname, old ,new):
#     source.data=dict(x=[], y=[])
#     update()

# date_pattern = ["%Y-%m-%d\n%H:%M:%S"]

# p.xaxis.formatter= DatetimeTickFormatter(
#     seconds=date_pattern,
#     minsec=date_pattern,
#     minutes=date_pattern,
#     hourmin=date_pattern,
#     hours=date_pattern,
#     days=date_pattern,
#     months=date_pattern,
#     years=date_pattern
    
# )

plot.xaxis.major_label_orientation=radians(80)
plot.xaxis.axis_label ="Time"
plot.yaxis.axis_label ="Value"

# Create Selection widget
# options= [("Data 1", "Data one"),("Data 2", "Data two")]
# select = Select(title="", value="Data 1", options=options)
# select.on_change("value", update_intermed)

# #Config Layout
# lay_out= layout([[p],[select]])
curdoc().title = "Streaming Data Example"
# curdoc().add_root(lay_out)
# curdoc().add_periodic_callback(update, 500)


