import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import os
from callbacks import register_overview_callbacks, register_find_movie_callbacks, register_result_page_callbacks
from pages import overview_page, find_movie_page, result_page


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.FONT_AWESOME])
# register_overview_callbacks(app)
register_find_movie_callbacks(app)
register_result_page_callbacks(app)

app.layout = html.Div([
    html.H1('Movie Analysis', style={'textAlign': 'center'}),
    dcc.Tabs(id="tabs-graph", value='find-movie-tab', children=[
        # dcc.Tab(overview_page, label='Overview', value='overview-tab', style={'fontSize': '32px'}, selected_style={'fontSize': '32px'}),
        dcc.Tab(find_movie_page, label='Find a movie', value='find-movie-tab', style={'fontSize': '32px'}, selected_style={'fontSize': '32px'}),
        dcc.Tab(result_page, label='Search result', value='search-result-tab', style={'fontSize': '32px'}, selected_style={'fontSize': '32px'}),
    ]),
    html.Br(),
    html.Div(id="page-content")
])


if __name__ == "__main__":
    app.run_server(debug=True, port=os.getenv('PORT', 3000))