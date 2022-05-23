from dash import dcc, html
import dash_bootstrap_components as dbc


find_movie_page = dbc.Container([
    dbc.Row([
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
                        dbc.Button(
                            "Advanced settings",
                            id="advanced-collapse-button",
                            className="mb-3",
                            color="primary",
                            n_clicks=0,
                        ),
                        dbc.Collapse([
                            dbc.Row([
                                dbc.Col([
                                    html.Div([
                                        dbc.Checkbox(value=True,
                                            id="search-by-keyword-checkbox",
                                            label="Search by keywords"
                                        ),
                                        dbc.Checkbox(value=True,
                                            id="fuzzy-match-checkbox",
                                            label="Fuzzy match"
                                        ),
                                        dbc.Checkbox(value=True,
                                            id="case-insensitive-checkbox",
                                            label="Case insensitive"
                                        ),
                                        dbc.Checkbox(value=True,
                                            id="prioritize-titles-checkbox",
                                            label="Prioritize titles over keywords"
                                        )
                                    ])
                                ], width=6),
                                dbc.Col([
                                    html.Div([
                                        dcc.Input(value=5,
                                            id="min-movie-rating-input",
                                            label="Minimum movie rating"
                                        ),
                                        dbc.Checkbox(value=True,
                                            id="fuzzy-match-checkbox1",
                                            label="Fuzzy match"
                                        ),
                                        dbc.Checkbox(value=True,
                                            id="case-insensitive-checkbox1",
                                            label="Case insensitive"
                                        ),
                                        dbc.Checkbox(value=True,
                                            id="prioritize-titles-checkbox1",
                                            label="Prioritize titles over keywords"
                                        )
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
    ]),
    dbc.Row([

    ], id='search-results')
], id='find-movie-page', style={'maxWidth':'100%'})