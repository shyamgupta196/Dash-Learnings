import dash
from dash.dependencies import Output,Input
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import datetime as dt
import random
import  plotly.graph_objs as go
from collections import deque
import time

xs = deque(maxlen=30)
xs.append(1)
ys = deque(maxlen=30)
ys.append(1)

#starting app 
app = dash.Dash(__name__)
#giving layout
app.layout = html.Div([
    html.H1(['Day4 plotting continuous input of data from source or something'], style={
        'color': 'green',
        'textAlign': 'center'
    }),
    dcc.Graph(id='graph', animate=True),


    dcc.Interval(
        id='update',
        interval=1
    )
])
#interesting question to search for 
# component property ---- figure and children whats the  difference???
# WHEN TO USE WHAT PROPERTY OF THE COMPONENTS 
#creating callbacks
#these are wrappers/decorators in the app
#the function declared will be called automatically called
#hence these are necessary.......

@app.callback(Output('graph', 'figure'),
               [Input('update', 'interval')])
def update_grapher(temp):
    global xs
    global ys

    opener = open('data.txt', 'r').read()
    lines = opener.split('\n')
    time.sleep(1)
    for line in lines:
        if len(line) > 0:
            x, y = line.split(',')
            xs.append(xs[-1]+int(x))
            ys.append(ys[-1]+(int(y)*random.normalvariate(8,3)))


    data = go.Scatter(x=list(xs),
                      y=list(ys),
                      mode='markers',
                      fill='tonexty')
    return {'data': [data], 'layout': go.Layout(xaxis=dict(range=[min(xs), max(xs)]),
                                                yaxis=dict(range=[min(ys), max(ys)]))}
if __name__ == '__main__':
    app.run_server(debug=True)
