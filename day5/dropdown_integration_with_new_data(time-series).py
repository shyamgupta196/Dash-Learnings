import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output,Input
import plotly.express as px
##import pandas_datareader as web
import pandas as pd
import datetime as dt

##stock = "AAPL"
# df = web.get_dailysummary_iex('AAPL', start=datetime.datetime(
# 2013, 1, 1), end=datetime.datetime.now())

# may be there is something wrong with the api of iex hence
# i have a downloaded dataset of TSLA from 2010 to today(2020) [month wise] so lets start
# with pandas reading our data

df = pd.read_csv('TSLA1.csv')

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1(['🔥🔥Day5 finale 🔥🔥'], style={
        'color': 'green',
        'textAlign': 'center',

    }),



    html.H3([
            ''' Monthly Data of TESLA since 2010
            (May be I put a Drop Down Next Time to filter all the dates between a range )
        '''
        ],
            style={
                'color':'#fffc00',
                'textAlign':'center'             
                }),
    html.Div([
        dcc.Graph(id='our_graph')
    ]),

    html.Div([
        html.Label(['Choose Years of Border Crossings into the USA:'],
                    style={'font-weight': 'bold'}),
        html.P(),
        dcc.RangeSlider(
            id='my-range-slider', # any name you'd like to give it
            marks={
                2010: '2010',     # key=position, value=what you see
                2012: '2012',
                2014: '2014',
                2018: '2018',
                2020: {'label': '2020', 'style': {'color':'#f50', 'font-weight':'bold'},
                },
            },
            step=1,                # number of steps between values
            min=2010,
            max=2020,
            value=[2010,2020],     # default value initially chosen
            dots=True,             # True, False - insert dots, only when step>1
            allowCross=False,      # True,False - Manage handle crossover
            disabled=False,        # True,False - disable handle
            pushable=2,            # any number, or True with multiple handles
            updatemode='drag',  # 'mouseup', 'drag' - update value method
            included=True,         # True, False - highlight handle
            vertical=False,        # True, False - vertical, horizontal slider
            verticalHeight=900,    # hight of slider (pixels) when vertical=True
            className='None',
            tooltip={'always visible':False,  # show current slider values
                     'placement':'bottom'},
            ),
    ]),

])

#---------------------------------------------------------------

@app.callback(
    Output('our_graph','figure'),
    [Input('my-range-slider','value')]
)

def build_graph(years):

    dff = df.loc[years[1]:years[0]]
##    dff = dff[(dff['Adj Close'])]
##    dff = dff[(dff[''])#print(dff[:5])

    fig = px.bar(dff, x="Open", y="Close",color='Volume')

    fig.update_layout(yaxis={'title':'Incoming Border Crossings'},
                      title={'text':'Border Crossing into the United States',
                      'font':{'size':28},'x':0.5,'xanchor':'center'})
    return fig
##----------------------------------------------------------------
##@app.callback(
##    Output('table-output','children'),
##    [Input('dates','value')])
##
##def tbl(year):
##
##    return  html.Table([
##        html.Thead([
##            html.Tr([
##                html.Th(i) for i in df.columns
##        
##        ])
##            ]),
##        html.Tbody([
##            html.Tr([
##                html.Td(df.iloc[i][col]) for col in df.columns])
##            for i in range(len(df.index))
##                
##                   if df.index])
##    ])

if __name__ == '__main__':
    app.run_server(debug=True)




















    
