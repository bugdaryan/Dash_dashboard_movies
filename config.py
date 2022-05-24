from MovieFinder import MovieFinder
import dotenv
import os

dotenv.load_dotenv()
MOVIE_INFO_API = os.environ['MOVIE_INFO_API']
MONGODB_URI = os.environ['MONGODB_URI_ATLAS']

case_insensitive_collation = { 'locale': 'en', 'strength': 2 }

find_button_clicks = {
    -1:0,
    1:0,
    2:0,
    3:0
}

movie_finder = MovieFinder()