from MovieAPIFinder import MovieAPIFinder
from glob import glob
import json
import config


class MovieFinder:
    def __init__(self):
        
        self.api_finder = MovieAPIFinder()
        movies = []
        
        for path in glob('data/top-movie-?.json'):
            with open(path, 'r') as f:
                movie_json = json.load(f)

            movies.append(movie_json)

        self.found_movie = None
        self.top_movies = movies
        self.search_result = []

    
    def find_movie(self, top_movie_num=None, **kwargs):

        if top_movie_num > 0:
            self.found_movie = self.top_movies[top_movie_num-1]