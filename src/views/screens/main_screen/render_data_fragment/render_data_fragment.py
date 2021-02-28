import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output

from src.bootstrap import app
from src.views.screens.main_screen.render_data_fragment.data_view_sections import source_data_list, price_chart, \
    app_storage_status, period_filter

layout = html.Div([
    dcc.Store(id='filtered-data-storage'),
    html.Div(id='content-area'),
])


@app.callback(
    Output('content-area', 'children'),
    Input('api-response-storage', 'data')
)
def init_view(data):
    if data:
        return html.Div([
            app_storage_status.layout,
            period_filter.layout,
            price_chart.layout,
            source_data_list.layout,
        ])
