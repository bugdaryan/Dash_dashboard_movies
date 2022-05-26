from MovieAPIFinder import MovieAPIFinder
from glob import glob
import json
import config
from pymongo import MongoClient


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
        self.search_results = []

    
    def find_movie(self, top_movie_num=None, **kwargs):
# ['input', 'search_by', 'min_year', 'max_year', 'min_rating', 'limit', 'fuzzy']
        if top_movie_num > 0:
            self.found_movie = self.top_movies[top_movie_num-1]
        else:
            if 'Title' in kwargs['search_by']:
                client = MongoClient(config.MONGODB_URI)
                db = client.movies
                movies = db.movies

                results = movies.find({'title': kwargs['input']}) \
                            .collation(config.case_insensitive_collation) \
                            .limit(kwargs['limit'])
                results = list(results)
                for movie in results:
                    api_info = self.api_finder.find_movie(movie['metadata']['imdb_id'])
                    movie['image'] = api_info['Poster']
                    movie['api_info'] = api_info
                self.search_results = list(results)

