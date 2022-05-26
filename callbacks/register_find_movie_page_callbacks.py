from dash.dependencies import Input, Output, State
import numpy as np
from dash import html, dcc
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import json
from glob import glob
from config import find_button_clicks, movie_finder
from collections import OrderedDict

def register_find_movie_page_callbacks(app):
    @app.callback([Output('top-movie-1', 'children'),
    Output('top-movie-2', 'children'),
    Output('top-movie-3', 'children')],
    [Input('find-movie-page', 'children')])
    def init_top_movies(children):

        movies = []
        for i, movie in enumerate(movie_finder.top_movies):
            overview_text = ', '.join([m['name'] for m in movie['cast'][:5]])
            movies.append([
                dbc.CardImg(src=movie['image'], top=True),
                dbc.CardBody([
                        html.H5(movie['title'], className="card-title"),
                        html.P([html.B('Cast: '), overview_text]),
                        dbc.Button("Find", color="primary", id=f'top-movie-{i+1}-find-btn', n_clicks=0),
                    ]
                )
            ])
        
        return movies

    @app.callback(Output('tabs-graph', 'value'),
    [Input('placeholder', 'children'),
    Input('top-movie-1-find-btn', 'n_clicks'),
    Input('top-movie-2-find-btn', 'n_clicks'),
    Input('top-movie-3-find-btn', 'n_clicks'),
    Input('find-movie-btn', 'n_clicks')],
    [State('movie-input', 'value'),
    State('search-by-dropdown', 'value'),
    State('min-movie-year-input', 'value'),
    State('max-movie-year-input', 'value'),
    State('min-movie-rating-input', 'value'),
    State('limit-search-input', 'value'),
    State('fuzzy-match-checkbox', 'value')])
    def find_movie_click(_, t1_btn, t2_btn, t3_btn, find_btn, input, *args):
        t = None 
        if find_button_clicks[1] != t1_btn:
            t = 1
            find_button_clicks[1] = t1_btn
        elif find_button_clicks[2] != t2_btn:
            t = 2
            find_button_clicks[2] = t2_btn
        elif find_button_clicks[3] != t3_btn:
            t = 3
            find_button_clicks[3] = t3_btn
        elif find_button_clicks[-1] != find_btn:
            t = -1
            find_button_clicks[-1] = find_btn
        
        options = dict(zip(['input', 'search_by', 'min_year', 'max_year', 'min_rating', 'limit', 'fuzzy'], [input]+list(args)))
        if not options['search_by']:
            options['search_by'] = ['Title']

        tab = 'find-movie-tab'
        if t and t > 0:
            tab = 'search-result-tab'
            movie_finder.find_movie(top_movie_num=t, **options)
        elif t == -1 and input:
            tab = 'results-tab'
            movie_finder.find_movie(top_movie_num=t, **options)

            inputs = [Input(f'go-to-movie-page-button-{i}', 'n_clicks') for i in range(len(movie_finder.search_results))]
            
            print('VVVVVVVVVVV')
            @app.callback(Output('placeholder', 'children'), inputs)
            def init_movie_buttons(*btns):
                print(btns)

                return None
            print('ZZZZZZZZZZZZZ')

            print('AAAA', len(movie_finder.search_results))

        elif not t and find_btn:
            # print(movie_finder.found_movie)
            print('AAAAA')
            tab = 'search-result-tab'
        
        return tab


    @app.callback(
        [Output("advanced-collapse", "is_open"),
        Output("advanced-collapse-button", "children")],
        [Input("advanced-collapse-button", "n_clicks")],
        [State("advanced-collapse", "is_open"),
        State("advanced-collapse-button", "children")],
    )
    def toggle_collapse(n, is_open, children):
        
        class_name = children[1]['props']['className']
        if class_name == 'fa-solid fa-angle-down':
            class_name = 'fa-solid fa-angle-up'
        else:
            class_name = 'fa-solid fa-angle-down'
        
        children = [children[0], html.I(className=class_name)]

        if n:
            return not is_open, children
        return is_open, children


        

        