import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/Weather2014-15.csv')

# Preparing data
new_df = df.groupby(['day', 'month']).max().reset_index()

data = [go.Heatmap(x=new_df['day'],
                  y=new_df['month'],
                  z=new_df['record_max_temp'],
                  colorscale='Jet')]

# Preparing layout
layout = go.Layout(title='The Maximum Record Temperature', xaxis_title="Day of the Week", yaxis_title="Month of the Year")

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='temperatureHeatmap.html')
