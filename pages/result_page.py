from dash import dcc, html
import dash_bootstrap_components as dbc
from config import movie_finder

result_page = dbc.Container([
    html.Br(),
    dbc.Row([
        dbc.Col(width=1),
        dbc.Col([
            dbc.CardImg(top=True, id='result-movie-image'),
        ], width=3),
        dbc.Col([
            dbc.Row(id='result-movie')
        ], width=6)
    ]),
    dbc.Row([

    ])
], id='result-page', style={'maxWidth':'100%'})