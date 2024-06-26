from spotify_connection import connect_to_spotify
import webbrowser
from win11toast import toast
import fontstyle

from spotify_functions import get_artist_suggestions

def open_web(arg, url):
    webbrowser.open_new_tab(url)
    
def getNotification(): 
    spotify = connect_to_spotify()    
    suggested_artist:list = get_artist_suggestions(spotify)    
    msg = f"Since you have listened to {list(suggested_artist[1])[0]}, we recommend you check out {suggested_artist[0][0]}"
    toast('Daily Spotify Suggestions', msg, on_click= lambda arg: open_web(arg=arg, url=suggested_artist[1][1][1]))
        
if __name__ == '__main__':
    getNotification() 
