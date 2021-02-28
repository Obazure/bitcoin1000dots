import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import State, Input, Output
from dash.exceptions import PreventUpdate

from src.bootstrap import app
from src.module.api_loader import data_api_load
from src.views.screens.main_screen.render_data_fragment import render_data_fragment

"""Create a dashboard app with Dash."""
layout = html.Div(
    children=[
        dcc.Store(id='api-response-storage'),

        html.Button(
            'Update Data',
            id='api-request-button',
            title='(currently it\'s only re-generate data set)',
            className="btn btn-primary"
        ),

        html.Div(className='mt-5 mb-5', children=[
            render_data_fragment.layout
        ]),
    ])


@app.callback(
    Output('api-response-storage', 'data'),
    Input('api-request-button', 'n_clicks'),
    State('api-response-storage', 'data')
)
def api_request(n_clicks, data):
    if data is None:
        return data_api_load()
    if n_clicks is None:
        raise PreventUpdate
    return data_api_load()
