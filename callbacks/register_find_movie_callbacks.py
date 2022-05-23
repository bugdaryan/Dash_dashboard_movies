from dash.dependencies import Input, Output, State
import numpy as np
from dash import html, dcc
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import json
from glob import glob
from config import find_button_clicks

def register_find_movie_callbacks(app):
    @app.callback([Output('top-movie-1', 'children'),
    Output('top-movie-2', 'children'),
    Output('top-movie-3', 'children')],
    [Input('find-movie-page', 'children')])
    def init_top_movies(children):
        movies = []
        movie_images = ['https://images.photowall.com/products/59586/pulp-fiction.jpg?h=699', 'https://m.media-amazon.com/images/I/41ekyDiO1ZL._AC_.jpg', 'https://collider.com/wp-content/uploads/i-origins-poster1.jpg']
        for i, path in enumerate(glob('data/top-movie-?.json')):
            with open(path, 'r') as f:
                movie_json = json.load(f)

            overview_text = ', '.join([m['name'] for m in movie_json['cast'][:5]])
            movies.append([
                dbc.CardImg(src=movie_images[i], top=True),
                dbc.CardBody([
                        html.H5(movie_json['title'], className="card-title"),
                        html.P([html.B('Cast: '), overview_text]),
                        dbc.Button("Find", color="primary", id=f'top-movie-{i+1}-find-btn', n_clicks=0),
                    ]
                )
            ])
        
        return movies

    @app.callback([Output('search-results', 'children')],
    [Input('top-movie-1-find-btn', 'n_clicks'),
    Input('top-movie-2-find-btn', 'n_clicks'),
    Input('top-movie-3-find-btn', 'n_clicks'),
    Input('find-movie-btn', 'n_clicks')],
    [State('movie-input', 'value')])
    def find_movie(t1_btn, t2_btn, t3_btn, find_btn, input):
        t = None 
        if find_button_clicks[1] != t1_btn:
            t = 'button 1 was pressed'
            find_button_clicks[1] = t1_btn
        if find_button_clicks[2] != t2_btn:
            t = 'button 2 was pressed'
            find_button_clicks[2] = t2_btn
        if find_button_clicks[3] != t3_btn:
            t = 'button 3 was pressed'
            find_button_clicks[3] = t3_btn
        if find_button_clicks[-1] != find_btn:
            t = 'find button was pressed'
            find_button_clicks[-1] = find_btn

        return [t]


    @app.callback(
        Output("advanced-collapse", "is_open"),
        [Input("advanced-collapse-button", "n_clicks")],
        [State("advanced-collapse", "is_open")],
    )
    def toggle_collapse(n, is_open):
        if n:
            return not is_open
        return is_open
        

        