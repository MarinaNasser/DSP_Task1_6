from bokeh.io import curdoc
from bokeh.models import ColumnDataSource, DatetimeTickFormatter, Select
from bokeh.layouts import layout
from bokeh.plotting import figure
from datetime import datetime
from math import radians
import numpy as np

p=figure(x_axis_type="datetime", width=900, height=350)

def create_value():
    draw= np.random.randint(0,2, size=200)
    steps= np.where(draw>0,1,-1)
    walk= steps.cumsum() #[-1,1]
    return walk[-1]

#Create data source
source= ColumnDataSource(dict(x=[],y=[]))

p.circle(x="x", y="y", color="firebrick" , line_color="firebrick", source=source)
p.line(x="x", y="y", source=source)

#Create Periodic Function
def update():
    new_data=dict(x=[datetime.now()], y=[create_value()])
    source.stream(new_data, rollover=200)
    p.title.text="Now Streaming %s Data" % select.value


#Callback function
def update_intermed(attrname, old ,new):
    source.data=dict(x=[], y=[])
    update()

date_pattern = ["%Y-%m-%d\n%H:%M:%S"]

p.xaxis.formatter= DatetimeTickFormatter(
    seconds=date_pattern,
    minsec=date_pattern,
    minutes=date_pattern,
    hourmin=date_pattern,
    hours=date_pattern,
    days=date_pattern,
    months=date_pattern,
    years=date_pattern
    
)

p.xaxis.major_label_orientation=radians(80)
p.xaxis.axis_label ="Date"
p.yaxis.axis_label ="Value"

#Create Selection widget
options= [("stock1", "stock one"),("stock2", "stocktwo")]
select = Select(title="Market Name", value="stock1", options=options)
select.on_change("value", update_intermed)

#Config Layout
lay_out= layout([[p],[select]])
curdoc().title = "Streaming Stock Data Example"
curdoc().add_root(lay_out)
curdoc().add_periodic_callback(update, 500)

