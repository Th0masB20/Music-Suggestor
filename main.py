from spotify_connection import connect_to_spotify
from winotify import Notification

from spotify_functions import get_artist_suggestions

def getNotification(): 
    spotify = connect_to_spotify()    
    suggested_artist:list = get_artist_suggestions(spotify)
    msg = f"Since you have listened to {list(suggested_artist[1])[0]}, we recommend you check out {suggested_artist[0]}"
    notification = Notification(app_id='Test Message', 
                                title='Daily spotify suggestion',
                                msg=msg, 
                                duration='short')
    notification.show()
    
if __name__ == '__main__':
    getNotification() 
