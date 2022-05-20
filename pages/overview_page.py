from dash.dependencies import Input, Output, State
import numpy as np
from dash import html, dcc
import dash_bootstrap_components as dbc
import pandas as pd


overview_page = dbc.Container([
    dbc.Row([
        dbc.Row([
            dbc.Row([
                dbc.Row([
                    dbc.Row([
                        dbc.Col([], width=5),
                        dbc.Col([html.Br(), html.H1('Average movie ratings'), html.Br(), html.H2('Average movie ratings over the years')], width=6)
                    ]),
                    dbc.Row([dcc.Graph(id='average-rating-over-time-graph')])
                ], id='average-rating-over-time'),
                dbc.Row([
                    dbc.Row([
                        dbc.Col([], width=5),
                        dbc.Col([html.H2('Average movie ratings by category'), html.Br()], width=6)
                    ]),
                    dbc.Row([
                        dbc.Row([
                            dbc.Col([], width=3),
                            dbc.Col([dcc.Dropdown(id='average-rating-category-dropdown', options=['action', 'horror', 'drama'], multi=True)], id='average-rating-category-dropdown-col', width=6),
                        ]),
                        dbc.Row([
                            dbc.Col([dcc.Graph(id='average-rating-by-category-graph')], id='average-rating-by-category', width=6),
                            dbc.Col([dcc.Graph(id='average-rating-by-top-categories-graph')], id='average-rating-by-top-categories', width=6),
                        ])
                    ])
                ]),
            ]),
        ]),
        dbc.Row([
            dbc.Row([
                dbc.Row([
                    dbc.Row([
                        dbc.Col([], width=5),
                        dbc.Col([html.Br(), html.H1('Number of movies'), html.Br(), html.H2('Number of movies over the years')], width=6)
                    ]),
                    dbc.Row([dcc.Graph(id='counts-over-time-graph')])
                ], id='counts-over-time'),
                dbc.Row([
                    dbc.Row([
                        dbc.Col([], width=5),
                        dbc.Col([html.H2('Number of movies by category'), html.Br()], width=6)
                    ]),
                    dbc.Row([
                        dbc.Row([
                            dbc.Col([], width=3),
                            dbc.Col([dcc.Dropdown(id='counts-category-dropdown', options=['action', 'horror', 'drama'], multi=True)], id='counts-category-dropdown-col', width=6),
                        ]),
                        dbc.Row([
                            dbc.Col([dcc.Graph(id='counts-by-category-graph')], id='counts-by-category', width=6),
                            dbc.Col([dcc.Graph(id='counts-by-top-categories-graph')], id='counts-by-top-categories', width=6),
                        ])
                    ])
                ]),
            ]),
            dbc.Row([
                dbc.Row([
                    dbc.Row([
                        dbc.Col([], width=5),
                        dbc.Col([html.Br(), html.H1('Average movie revenue'), html.Br(), html.H2('Average movie revenue over the years')], width=6)
                    ]),
                    dbc.Row([dcc.Graph(id='average-revenue-over-time-graph')])
                ], id='average-revenue-over-time'),
                dbc.Row([
                    dbc.Row([
                        dbc.Col([], width=5),
                        dbc.Col([html.H2('Average movie revenue by category'), html.Br()], width=6)
                    ]),
                    dbc.Row([
                        dbc.Row([
                            dbc.Col([], width=3),
                            dbc.Col([dcc.Dropdown(id='average-revenue-category-dropdown', options=['action', 'horror', 'drama'], multi=True)], id='average-revenue-category-dropdown-col', width=6),
                        ]),
                        dbc.Row([
                            dbc.Col([dcc.Graph(id='average-revenue-by-category-graph')], id='average-revenue-by-category', width=6),
                            dbc.Col([dcc.Graph(id='average-revenue-by-top-categories-graph')], id='average-revenue-by-top-categories', width=6),
                        ])
                    ])
                ]),
            ])
        ])
    ]),
], id='overview-page', style={'maxWidth':'100%'})

