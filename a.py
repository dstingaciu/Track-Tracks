import spotipy
from spotipy import util

username = "zap12341"
client_id = "da6e7e0d474a47b797943c65bfaa94fb"
client_S = '3a5ad8a8a63d4733b56bfb638c2fc8d8'
redUrl = 'https://dstingaciu.github.io/Track-Tracks/'

token = util.prompt_for_user_token(username,'user-read-private user-read-email',client_id,client_S,redUrl)

print ("Done")