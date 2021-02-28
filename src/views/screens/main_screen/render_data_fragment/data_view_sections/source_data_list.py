from dash.dependencies import Input, Output
import dash_html_components as html
import dash_table

from src.bootstrap import app
from src.utils.format_timestamp_to_date import format_timestamp_to_date

layout = html.Div([
    html.H5('List of prices sorted by dates.', className='text-center'),
    dash_table.DataTable(id='price-date-table', columns=[
        {'name': '#ID', 'id': 'id'},
        {'name': 'Price', 'id': 'value'},
        {'name': 'Date', 'id': 'date'}
    ]),
])


@app.callback(
    Output('price-date-table', 'data'),
    Input('filtered-data-storage', 'data'),
)
def on_data_set_table(data):
    if data:
        data = [
            {'id': index + 1, 'value': str(val['value']) + " USD", 'date': format_timestamp_to_date(val['date'])}
            for index, val in enumerate(data)
        ]

        return data
    return []
