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
from dash import Dash, dash_table


def register_movie_page_callbacks(app):
    @app.callback([Output('result-movie', 'children'),
    Output('result-movie-image', 'src')],
    [Input('tabs-graph', 'value')])
    def init_result_movie(tab):
        result_movie = None
        image = None


        if tab == 'search-result-tab':
            movie = movie_finder.found_movie

            imdb_page = f"https://www.imdb.com/title/{movie['metadata']['imdb_id']}"
            title = movie['title']
            year = [html.B('Year: '), movie['api_info']['Year']]
            image = movie['image']
            duration  = [html.B('Duration: '), movie['api_info']['Runtime']]
            genre = [html.B('Genre: '), movie['api_info']['Genre']]
            director = [html.B('Director: '), movie['api_info']['Director']]

            cast = [html.B('Cast: '), ', '.join([c['name'] for c in movie['cast'][:5]]),
                html.Div([
                    dbc.Button(
                        ["Expand Cast\t", html.I(className="fa-solid fa-angle-up")],
                        id="search-result-cast-collapse-button",
                        className="mb-3",
                        color="primary",
                        n_clicks=0,
                    ),
                    dbc.Collapse(
                        [html.P([html.B(c['name']), ' - ', c['character'], html.Br()]) for c in movie['cast']],
                        id="search-result-cast-collapse",
                        is_open=False,
                    ),
                ], style={'fontSize':'16px'})]

            crew = [html.B('Crew: ', style={'fontSize':'24px', 'marginRight':'15px'}), html.Div([
                dbc.Button(
                    ["Expand Crew\t", html.I(className="fa-solid fa-angle-up")],
                    id="search-result-crew-collapse-button",
                    className="mb-3",
                    color="primary",
                    n_clicks=0,
                ),
                dbc.Collapse(
                    [html.P([html.B(c['name']), ' - ', c['job'], html.Br()]) for c in movie['crew']],
                    id="search-result-crew-collapse",
                    is_open=False,
                ),
            ])]
            
            description = [html.B('Overview: '), html.Br(), movie['metadata']['overview']]
            imdb_rating = [html.B('IMDB rating: '), movie['api_info']['imdbRating']]
            metacritic_rating = [html.B('Metacritic rating: '), movie['api_info']['Metascore']]

            items = movie['vocab'].items()
            keywords_df = pd.DataFrame({'Word': [i[0] for i in items], 'Count': [i[1] for i in items]}).sort_values('Count', ascending=False)
            keywords_df = keywords_df[~keywords_df['Word'].str.isnumeric()]
            keywords_df = keywords_df[keywords_df['Word'].str.strip().str.len() != 0]

            keywords = [html.B('Top 100 words: ', style={'fontSize':'24px', 'marginRight':'15px'}), html.Div([
                dbc.Button(
                    ["Expand Top Words\t", html.I(className="fa-solid fa-angle-up")],
                    id="search-result-vocab-collapse-button",
                    className="mb-3",
                    color="primary",
                    n_clicks=0,
                ),
                dbc.Collapse(
                    dash_table.DataTable(keywords_df.iloc[:100].to_dict('records'), [{"name": i, "id": i} for i in keywords_df.columns], page_size=20),
                    id="search-result-vocab-collapse",
                    is_open=False,
                ),
            ])]


            result_movie = [
                dcc.Link(html.H1(title, style={'fontSize':'64px'}), href=imdb_page),
                html.P(year, style={'fontSize':'24px'}),
                html.P(duration, style={'fontSize':'24px'}),
                html.P(genre, style={'fontSize':'24px'}),
                html.P(director, style={'fontSize':'24px'}),
                html.P(description, style={'fontSize':'24px'}),
                html.P(imdb_rating, style={'fontSize':'24px'}),
                html.P(metacritic_rating, style={'fontSize':'24px'}),
                html.P(cast, style={'fontSize':'24px'}),
                html.P(crew, style={'display':'inline-flex'}),
                html.P(keywords, style={'display':'inline-flex'}),
            ]

        return result_movie, image


    
    @app.callback(
        [Output("search-result-crew-collapse", "is_open"),
        Output("search-result-crew-collapse-button", "children")],
        [Input("search-result-crew-collapse-button", "n_clicks")],
        [State("search-result-crew-collapse", "is_open"),
        State("search-result-crew-collapse-button", "children")],
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


    @app.callback(
        [Output("search-result-cast-collapse", "is_open"),
        Output("search-result-cast-collapse-button", "children")],
        [Input("search-result-cast-collapse-button", "n_clicks")],
        [State("search-result-cast-collapse", "is_open"),
        State("search-result-cast-collapse-button", "children")],
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


    @app.callback(
        [Output("search-result-vocab-collapse", "is_open"),
        Output("search-result-vocab-collapse-button", "children")],
        [Input("search-result-vocab-collapse-button", "n_clicks")],
        [State("search-result-vocab-collapse", "is_open"),
        State("search-result-vocab-collapse-button", "children")],
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