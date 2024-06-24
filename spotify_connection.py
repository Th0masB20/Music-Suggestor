import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv

load_dotenv()

port = 3000
redirect_url = f"http://localhost:3000"
client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')

def connect_to_spotify():
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_url, scope=['user-read-private', 'user-read-email']))
    return sp