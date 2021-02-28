import dash

from src.views.layout import header
from src.views.screens import error_screen
from src.views.screens.main_screen import main_screen


def route(app):
    """App Routing by Url"""
    app.layout = header.layout

    @app.callback(
        dash.dependencies.Output('page-content', 'children'),
        dash.dependencies.Input('url', 'pathname')
    )
    def display_page(pathname):
        if pathname == '/':
            return main_screen.layout
        return error_screen.layout
