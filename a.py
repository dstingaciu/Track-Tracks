import spotipy

from spotipy import util

username = "zap12341"
client_id = "da6e7e0d474a47b797943c65bfaa94fb"
client_S = '3a5ad8a8a63d4733b56bfb638c2fc8d8'
redUrl = 'https://dstingaciu.github.io/Track-Tracks/'

token = util.prompt_for_user_token(username,'user-read-currently-playing',client_id,client_S,redUrl)

if token:
	sp = spotipy.Spotify(auth = token)
	cp = sp.currently_playing(market = "CA")
	content = cp.get('item')
	if(cp["is_playing"] == False):
		print ("You are currently not playing anything")
	else:
		print ("You are currently playing "+content["name"]+" by "+ content["artists"][0]["name"])
