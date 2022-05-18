import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import os
from callbacks import register_overview_callbacks, register_find_movie_callbacks
from pages import overview_page, find_movie_page

app = dash.Dash(__name__)
register_find_movie_callbacks(app)
register_overview_callbacks(app)
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),html.Div(id="page-content")
    ])


@app.callback(Output('navbar', 'children'),
                [Input('page-content', 'children')],
                [State('url', 'pathname')])
def update_navlinks(children, pathname):
    nav_items = {
        "/overview":dbc.NavItem(dbc.NavLink("Overview", href="/overview")),
        "/find_movie":dbc.NavItem(dbc.NavLink("Find Movie", href="/find_movie"))
    }
    if pathname in nav_items.keys():
        nav_items[pathname].active=True

    return list(nav_items.values())


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_current_page(pathname):

    if pathname == '/overview':
        return overview_page
    elif pathname == '/find_movie':
        return find_movie_page

    return overview_page


if __name__ == "__main__":
    app.run_server(debug=True, port=os.getenv('PORT', 3000))