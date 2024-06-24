from spotify_connection import connect_to_spotify
from winotify import Notification

from spotify_functions import get_user_playlists

def getNotification(): 
    spotify = connect_to_spotify()
    notification = Notification(app_id='Test Message', 
                                title='Daily spotify suggestion',
                                msg='Check out this new music playlist', 
                                duration='short')
    get_user_playlists(spotify)
    notification.show()
    
if __name__ == '__main__':
    getNotification() 
