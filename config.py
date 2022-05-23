import dotenv
import os

dotenv.load_dotenv()

MONGODB_URI = os.environ['MONGODB_URI']

find_button_clicks = {
    -1:0,
    1:0,
    2:0,
    3:0
}