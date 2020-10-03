import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px
import pandas WebCrawler
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv('gdpdata.csv')

colors = {
    'background': '#000000',
    'text': '#DAA520',
    'head': '#FFFF00'

}

# fig = plt.figure()
# ax = fig.add_subplot(111)
fig = px.area(df, y='GDP_Growth', x='date')

fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)


def generate_table(dataframe, max_rows):
    return html.Table(style={
        'textAlign': 'center'}, children=[
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody(children=[
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ])for i in range(max_rows)
        ],
            style={
            'textAlign': 'center'
        })
    ],

    )


app.layout = html.Div(style={'backgroundColor': colors['background'], 'textAlign': 'center'}, children=[
    html.H2(children='Table Of Data',
            style={
                'color': colors['head'],
                'textAlign': 'left'
            }),
    generate_table(df, 13),


    html.H1(children='area graph of gdp of India',
            style={
                'textAlign': 'center',
                'color': colors['text']
            }
            ),

    html.Div(children='''
        DASH: a dash interactive web
        ''',
             style={
                 'textAlign': 'center',
                 'color': colors['text']
             }
             ),


    dcc.Graph(id='example_graph',
              figure=fig,
              )])


if __name__ == '__main__':
    app.run_server(debug=True)
