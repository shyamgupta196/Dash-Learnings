# this is a simple app used for calculate the area  of the circle from radius

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import math
import plotly.express as px
import pandas as pd

# data
df = pd.read_csv('titanic-cleaned.csv')


app = dash.Dash(__name__)


app.layout = html.Div([
    html.H3(children=[
        '''first trial of the callback with area calculation of the circle
    taking radius as input!!'''
    ]),
    html.Div(['Enter Radius: ', dcc.Input(id='my input',
                                          value='initital value',
                                          type='number')]),
    html.Br(),
    html.Div(id='my output')
])
# html.Br()

##    html.H2('using Titanic dataset to plot the Data '),

# we are tryin to take input of the columns and plot a distplot and scatter
# plot of the data
'''
continued on day 3
check more on day 3
'''


# html.Div(['Enter Column Name: ',dcc.Input(id='grf input',
##        value='col val',
# type='text'
# )]),
##    html.Div('Resulting Graph',id='Output Graph')
##
# ])

@app.callback(
    Output(component_id='my output', component_property='children'),
    [Input(component_id='my input', component_property='value')])
##    Output('Output Graph','children'),
# [Input('grf input','value')])
def update_area_cal(r):
    try:
        return math.pi*(r*r)
    except:
        return 'some error'


if __name__ == '__main__':
    app.run_server(debug=True)
