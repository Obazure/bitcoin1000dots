import dash_html_components as html
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate

from src.bootstrap import app

layout = html.Div(className='mt-5 mb-5', children=[
    html.P(id="app-storage-status"),
    ])


@app.callback(
    Output('app-storage-status', 'children'),
    [
        Input('api-response-storage', 'data'),
        Input('filtered-data-storage', 'data')
    ]
)
def on_data_change_update_graph(api_storage, filtered_storage):
    message = ''
    if api_storage is None and filtered_storage is None:
        raise PreventUpdate

    if api_storage is not None:
        message += 'Overall %s records has been received from api. ' % len(api_storage)

    if filtered_storage is not None:
        message += 'Number of filtered %s records. ' % len(filtered_storage)

    return message


