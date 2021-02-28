import dash_core_components as dcc
import dash_html_components as html

layout = html.Div(
    children=[
        dcc.Location(id='url', refresh=False),
        html.Nav(
            className='navbar navbar-expand-lg navbar-light bg-light',
            children=[
                html.Div(className='container', children=[
                    dcc.Link('BTC prices chart example', className='navbar-brand', href='/'),
                ])
            ]
        ),
        html.Div(
            className='container',
            children=[
                html.H1("BTC price chart and linear equation!", className='text-center'),
                html.Div(id='page-content')
            ]
        )
    ])
