from sqlalchemy.exc import SQLAlchemyError
from db.db_connection import *


# Class for CRUD operations with playlists
class PlaylistCrud:
    def __init__(self, user_id):
        self.user_id = user_id

    # Method for adding a new playlist to our database
    def add_playlist(self, playlist_name):
        try:
            # Creating a new Playlists object
            playlist_to_add = Playlists(name=playlist_name, use_id=self.user_id)
            # Adding new playlist to the session and committing
            session.add(playlist_to_add)
            session.commit()
            return {
                "success": True,
                "message": "Successfully added the playlist"
            }
        except Exception as e:
            # Logging the error if it occurrs
            logging.exception('An error occurred')
            return {
                "success": False,
                "message": "Something went wrong while adding the playlist"
            }

    # Method for removing a playlist
    def remove_playlist(self, playlist_name):
        try:
            # Getting the playlist user wants to remove from the database
            playlist_to_remove = session.query(Playlists).filter_by(name=playlist_name, user_id=self.user_id).first()
            # Removing the playlist and committing
            session.delete(playlist_to_remove)
            session.commit()
            return {
                "success": True,
                "message": "Successfully removed playlist"
            }
        except SQLAlchemyError as e:
            # Logging the error if it occurred
            logging.exception('Error removing playlist')
            return {
                "success": False,
                "message": "An error occurred while removing the playlist"
            }

    # Method for changing the playlist name
    def change_playlist(self, playlist_name, new_name):
        try:
            # Querying the playlist user wants to change from the database
            playlist_to_change = session.query(Playlists).filter_by(name=playlist_name).first()
            # Making sure there is a playlist with inputted name
            if playlist_to_change is None:
                return {
                    "success": False,
                    "message": "Playlist does not exist"
                }
            else:
                # Changing the playlist name and committing
                playlist_to_change.name = new_name
                session.commit()
            return {
                "success": True,
                "message": "Successfully changed the playlist name"
            }
        except SQLAlchemyError as e:
            # Logging error if it occurred
            logging.exception('Error changing playlist')
            return {
                "success": False,
                "message": "An error occurred while changing the playlist name"
            }

    # Method for showing playlists
    def show_playlists(self):
        try:
            # Querying all the playlists from database and storing them into a dict
            playlists = session.query(Playlists).filter_by(user_id=self.user_id).all()
            dict = {}
            # Iterating through playlists and storing playlists data into a dict
            for playlist in playlists:
                dict[playlist.id] = playlist.name
            # Returning the dict
            return {
                "success": True,
                "message": "Successfully showed the playlists",
                "data": dict
            }
        except SQLAlchemyError as e:
            # Logging the error if it occurred
            logging.exception('Error showing playlists')
            return {
                "success": False,
                "message": "An error occurred while showing the playlists"
            }