from dash.dependencies import Input, Output, State
import numpy as np
from dash import html, dcc
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import json
from config import movie_finder

def register_results_page_callbacks(app):
    @app.callback([Output('results-page', 'children')],
    [Input('tabs-graph', 'value')])
    def init_results(tab):
        children = None
        if tab == 'results-tab':
# ############################################################
#             with open('data/top-movie-2.json', 'r') as f:
#                 fc = json.load(f)

#                 search_num = 0
#                 movie_finder.search_results = [fc]*search_num
# ############################################################
            if len(movie_finder.search_results) > 0:
                num_cols = 6

                children = [html.Br()]
                column = [dbc.Col(width=2)]
                # inputs = [Input(f'go-to-movie-page-button-{i}', 'n_clicks') for i in range(len(movie_finder.search_results))]
                
                # @app.callback(Output('placeholder', 'children'), inputs)
                # def init_movie_buttons(*btns):
                #     print(btns)

                #     return None

                # def register_movie_button(i):
                #     print('BBBBBBBBB')
                #     @app.callback(Output('placeholder', 'children'),
                #     Input(f'go-to-movie-page-button-{i}', 'n_clicks'))
                #     def set_movie_id(n):
                #         print('AAAAAAAAAAAAA')
                #         if n:
                #             movie_finder.found_movie = movie_finder.search_results[i]
                        
                #         return ''
                
                for i, movie in enumerate(movie_finder.search_results):
                    # @app.callback(Output('placeholder', 'children'),
                    #     Input(f'go-to-movie-page-button-{i}', 'n_clicks'))
                    # def set_movie_id(n):
                    #     if n:
                    #         print('AAAAAAAAAAAAA')
                    #         movie_finder.found_movie = movie_finder.search_results[i]


                    column.append(
                        dbc.Col([
                            dbc.Card([
                                dbc.CardImg(src=movie['image'], top=True),
                                dbc.CardBody(
                                    [
                                        html.H4(movie['title'], className="card-title"),
                                        html.P(movie['metadata']['overview'], className="card-text"),
                                        dbc.Button("Go to movie page", id=f'go-to-movie-page-button-{i}', color="primary"),
                                    ]
                                ),
                            ],
                            style={"width": "18rem"},
                        )], width=1, style={'marginRight':'88px', 'marginBottom':'22px'})
                    )

                    if len(column) % num_cols == 0 or i == len(movie_finder.search_results) - 1:
                        children.append(dbc.Row(column))
                        column = [dbc.Col(width=2)]

            else:
                children = [html.Br(), dbc.Row([
                    dbc.Col(width=4),
                    dbc.Col([html.H1('Oops, couldnt find any movie :/')], width=3)
                ])]
                

        return [children]


    # @app.callback(Output('placeholder', 'children'), eval(inputs))
    # def init_movie_buttons(*btns):
    #     print(btns)

    #     return None

    # def register_movie_button(i):
    #     print('BBBBBBBBB')
    #     @app.callback(Output('placeholder', 'children'),
    #     Input(f'go-to-movie-page-button-{i}', 'n_clicks'))
    #     def set_movie_id(n):
    #         print('AAAAAAAAAAAAA')
    #         if n:
    #             movie_finder.found_movie = movie_finder.search_results[i]
            
    #         return ''
    
    # [register_movie_button(i) for i in range(len(movie_finder.search_results))]

    
    # @app.callback(Output('tabs-graph', 'value'),
    # Input('go-to-movie-page-button', 'n_clicks'),
    # State('tabs-graph', 'value'))
    # def go_to_movie_page_click(n, tab):
    #     if n:
    #         tab = 'search-result-tab'
    #         # movie_finder.found_movie
        
    #     return tab

