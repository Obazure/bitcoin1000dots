import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input, State

from src.bootstrap import app

layout = html.Div(className='mt-5 mb-5', children=[
    dcc.Dropdown(
                id='period_dropdown',
                options=[
                    {'label': '15 min', 'value': '15m'},
                    {'label': '1 hour', 'value': '1h'},
                    {'label': '1 day', 'value': '1d'},
                ],
                value='15m'
            )
    ])


@app.callback(
    Output('filtered-data-storage', 'data'),
    Input('period_dropdown', 'value'),
    State('api-response-storage', 'data'),
)
def on_data_filtered(filter_period, api_storage):
    filtered = api_storage

    def filtered_by_period(scope, step):
        filtered_data = []
        for obj in reversed(scope):
            if len(filtered_data) == 0:
                filtered_data.insert(0, obj)
            else:
                if int(filtered_data[0]['date']) - int(obj['date']) > step:
                    filtered_data.insert(0, obj)
        return filtered_data

    if filter_period == '1h':
        filtered = filtered_by_period(api_storage, 60*60)  # 1 hour
    if filter_period == '1d':
        filtered = filtered_by_period(api_storage, 60*60*24)  # 1 day
    return filtered
