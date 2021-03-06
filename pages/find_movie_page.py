from dash import dcc, html
import dash_bootstrap_components as dbc


find_movie_page = dbc.Container([
    html.Label('', id='placeholder'),
    html.Br(),
    dbc.Row([
        dbc.Col(width=4),
        dbc.Col([
            dbc.Row([
                dbc.Row([html.Br(), dbc.Label('Enter a movie name', style={'fontSize':'24px'})]), 
                dbc.Row([
                    dbc.Col([dbc.Input(id='movie-input', style={'fontSize':'24px'})], width=8),
                    dbc.Col([dbc.Button('Find', id='find-movie-btn', n_clicks=0, style={'fontSize':'24px', 'textAlign':'center'})], width=4)
                ])
            ]),
            html.Br(),
            dbc.Row([
                html.Div([
                    dbc.Button([
                        "Advanced settings\t", html.I(className="fa-solid fa-angle-up")],
                        id="advanced-collapse-button",
                        className="mb-3",
                        color="primary",
                        n_clicks=0,
                    ),
                    dbc.Collapse([
                        dbc.Row([
                            dbc.Col([
                                html.Div([
                                    html.Div([
                                        dbc.Label('Select options to search by and priority'),
                                        dcc.Dropdown(
                                            id='search-by-dropdown', 
                                            options=['Title', 'Cast', 'Crew', 'Keywords'], 
                                            value=['Title', 'Cast', 'Crew', 'Keywords'], 
                                            multi=True
                                        )
                                    ]),
                                    html.Br(),
                                    dbc.Row([
                                        dbc.Col([
                                            dbc.Input(value=1982,
                                                min=1982,
                                                id="min-movie-year-input",
                                                type='number'
                                            )
                                        ], width=4),
                                        dbc.Col([
                                            dbc.Label("Minimum movie release year")
                                        ], width=6)
                                    ]),
                                    html.Br(),
                                    dbc.Row([
                                        dbc.Col([
                                            dbc.Input(value=2017,
                                                max=2017,
                                                id="max-movie-year-input",
                                                type='number'
                                            )
                                        ], width=4),
                                        dbc.Col([
                                            dbc.Label("Maximum movie release year")
                                        ], width=6)
                                    ]),
                                ])
                            ], width=6),
                            dbc.Col([
                                html.Div([
                                    dbc.Row([
                                        dbc.Col([
                                            dbc.Input(value=0,
                                                id="min-movie-rating-input",
                                                type='number'
                                            )
                                        ], width=4),
                                        dbc.Col([
                                            dbc.Label("Minimum movie rating")
                                        ], width=6)
                                    ]),
                                    html.Br(),
                                    dbc.Row([
                                        dbc.Col([
                                            dbc.Input(value=30,
                                                id="limit-search-input",
                                                type='number'
                                            )
                                        ], width=4),
                                        dbc.Col([
                                            dbc.Label("Limit search")
                                        ], width=6)
                                    ]),
                                    html.Br(),
                                    dbc.Checkbox(value=True,
                                        id="fuzzy-match-checkbox",
                                        label="Fuzzy match"
                                    ),
                                    html.Br(),
                                ])
                            ], width=6)
                        ])
                    ],
                        id="advanced-collapse",
                        is_open=False,
                    ),
                ])

            ])
        ], width=4),
    ]),
    html.Br(),
    html.Br(),
    dbc.Row([
        dbc.Row([
            dbc.Col(width=5),
            dbc.Col(html.H3('Top movies'), width=2),
        ]),
        dbc.Row([
            dbc.Col(width=3),
            dbc.Col([dbc.Card(id='top-movie-1')], width=2),
            dbc.Col([dbc.Card(id='top-movie-2')], width=2),
            dbc.Col([dbc.Card(id='top-movie-3')], width=2)
        ])
    ])
], id='find-movie-page', style={'maxWidth':'100%'})