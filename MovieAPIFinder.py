import config
import requests

class MovieAPIFinder:
    def __init__(self):
        self.base_url = config.MOVIE_INFO_API

    
    def find_movie(self, imdb_id):
        res = requests.get(self.base_url.format(imdb_id))

        res_json = res.json()
        
        return res_json