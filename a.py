import spotipy
from spotipy import util

username = input("Enter your Spotify Username: ")
client_id = "da6e7e0d474a47b797943c65bfaa94fb"
client_S = '3a5ad8a8a63d4733b56bfb638c2fc8d8'

util.prompt_for_user_token(username,scope=None,client_id,client_S, )