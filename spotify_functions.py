from spotipy import Spotify
import json

def get_user_playlists(sp:Spotify):
    playlist_data = sp.current_user_playlists(5)
    file = open('text.json', 'w');
    file.write(json.dumps(playlist_data))
    file.close()
    for playlists in playlist_data['items']:
        print(playlists['name'])
    
