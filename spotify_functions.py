from spotipy import Spotify
import json
import random

#gest your playlists
def get_user_playlists(sp:Spotify) -> dict:
    playlist_data:dict = sp.current_user_playlists(5)
    return playlist_data['items']

#gets all songs in a random playlist
def get_songs_in_playlist(sp:Spotify) -> dict:
    your_playlists:dict = get_user_playlists(sp);
    random_playlist:dict = random.choice(your_playlists)
    songs_in_playlist:dict = sp.playlist_items(random_playlist['id'])
    return songs_in_playlist
    
#from the playlist, get the artists of each song
def get_all_artists_in_album(sp:Spotify) -> dict:
    songs_in_playlist = get_songs_in_playlist(sp)
    artist_dic:dict = {}
    for songs in songs_in_playlist['items']:
        name:str = songs['track']['album']['artists'][0]['name']
        id:str = songs['track']['album']['artists'][0]['id']   
        url:str = songs['track']['album']['artists'][0]['external_urls']['spotify']
        artist_dic[name] = [id, url]
        
    return artist_dic

#gets a random artist and suggestes other artists similar to them
def get_suggestions(sp:Spotify) -> dict: 
    artist_in_playlist:dict = get_all_artists_in_album(sp)
    random_artist:str = random.choice(list(artist_in_playlist))
    url = f'https://api.spotify.com/v1/artists/{artist_in_playlist[random_artist][0]}/related-artists'
    suggestions = sp._get(url)
    suggestions['based_on'] = {random_artist:artist_in_playlist[random_artist]}
    return suggestions

def get_suggested_artists(sp:Spotify) -> list:
    suggested_dict:dict = get_suggestions(sp)
    suggested_artists:list = [{}, {}]
    
    for artist in suggested_dict['artists']:
        name = artist['name']
        id = artist['id']
        url = artist['external_urls']['spotify']
        suggested_artists[0][name] = [id, url]
    
    suggested_artists[1]['based_on'] = suggested_dict['based_on']
    return suggested_artists
    
def get_artist_suggestions(sp:Spotify):
    suggested_artists:list = get_suggested_artists(sp)
    file = open('songs.json', 'w')
    file.write(json.dumps(suggested_artists));
    file.close()
    random_suggested_artist = [list, {str: list}] 
    random_artist = random.choice(list(suggested_artists[0]))
    random_suggested_artist[0] = [random_artist, suggested_artists[0][random_artist]]
    
    based_on_artist = list(suggested_artists[1]['based_on'])[0]
    random_suggested_artist[1] = [based_on_artist, suggested_artists[1]['based_on'][based_on_artist]]
    return random_suggested_artist