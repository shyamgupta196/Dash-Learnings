import dash
import dash_core_components as dcc
import dash_html_components as html
# datareader will be used in further days
##import pandas_datareader.data as web
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output

##df = pd.read_csv('titanic-cleaned.csv')


app = dash.Dash()

app.layout = html.Div([
    html.H1('Day 3 app With User input Based Data Plotting '),
    html.Div(['Note: the Data is plotted against age column hence will produce a Straight line']),
     html.Div(['Enter the Value of the Column To Plot',dcc.Input(
            id='Name-input',type='text'
        )]),
    html.Br(),


    html.Div(id='Output')],

    style={
        'color':'#b39029',
        'textAlign':'center'
        })

@app.callback(
    Output(component_id='Output',component_property='children'),
    [Input(component_id='Name-input',component_property='value')]
    )

def grapher(col):
    df = pd.read_csv('titanic-cleaned.csv')
    
    if col:
        return dcc.Graph(id='bar graph',figure=px.scatter(df,x = df['Age'], y = df[col],color='Pclass'))
    elif col=='ls':
        return df.columns
        
if __name__ == '__main__':
    app.run_server(debug=True)
    










