import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_credentials_manager = SpotifyClientCredentials(client_id='8f136fd89ed141f787a74b0a26a801dc', client_secret='5168366b750e4e8f802ba9f8d6e6b7cd')
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
results = sp.search(q='genre:rap', type='track', limit=50)
tracks = []
offset = 0
while len(tracks) < 2000:
    results = sp.search(q='genre:rap', type='track', limit=50, offset=offset)
    tracks += results['tracks']['items']
    offset += 50
list_tracks = []

with open("list_songs_2000.txt", "w") as f:
    for track in tracks:
        track_name = track['name']
        track_id = track['id']
        f.write(str(track_name) + " " + str(track_id) + " " + str(track['external_urls']['spotify']) + "\n")