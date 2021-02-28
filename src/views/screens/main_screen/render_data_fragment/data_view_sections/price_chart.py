import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from src.bootstrap import app
from src.module.equation_line import equation_line
from src.utils.format_timestamp_to_date import format_timestamp_to_date

layout = html.Div(className='mt-5 mb-5', children=[
    dcc.Graph(id='price-graph'),
])


@app.callback(
    Output('price-graph', 'figure'),
    Input('filtered-data-storage', 'data')
)
def on_data_change_update_graph(data):
    figure = {
        'layout': {
            'title': 'BTC in USD price chart',
            'height': 800,
            'yaxis': {'automargin': True},
            'xaxis': {'automargin': True}
        }
    }

    if data:
        equation_x, equation_y = equation_line(data, 'date', 'value')
        equation_x = [format_timestamp_to_date(x) for x in equation_x]

        price_y, price_x = [], []
        for field in data:
            price_y.append(field['value'])
            price_x.append(format_timestamp_to_date(field['date']))

        figure['data'] = [
            {'x': price_x, 'y': price_y, 'type': 'linear', 'name': 'BTC/USD'},
            {'x': equation_x, 'y': equation_y, 'type': 'linear', 'name': 'Equation line'}
        ]

    return figure
