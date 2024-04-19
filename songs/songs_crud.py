from sqlalchemy.exc import SQLAlchemyError
from db.db_connection import *


class SongsCrud:
    def __init__(self, user_id):
        self.user_id = user_id

    def add_song(self, data):
        try:
            # Creating a new Songs object with the given details.
            song_to_add = Songs(name=data['song_name'], artist=data['song_artist'], album=data['song_album'],
                                duration=data['song_duration'], genre_id=data['genre_id'], user_id=self.user_id,
                                playlist_id=data['playlist_id'])
            session.add(song_to_add)  # Adding the new song to the session.
            session.commit()  # Committing the transaction.
            return {
                "success": True,
                "message": "Successfully added the song"
            }
        except SQLAlchemyError as e:
            logging.exception("Error adding song")  # Logging exception if error occurs.
            return {
                "success": False,
                "message": "An error occurred while adding the song"
            }
    # Method to remove a song
    def remove_song(self, song_name):
        try:
            song_to_remove = session.query(Songs).filter_by(name=song_name).first()  # Querying the song to remove.
            session.delete(song_to_remove)  # Deleting the song from the session.
            session.commit()  # Committing the transaction.
            return {
                "success": True,
                "message": "Successfully removed the song"
            }
        except SQLAlchemyError as e:
            logging.exception("Error removing song")  # Logging exception if error occurs.
            return {
                "success": False,
                "message": "An error occurred while removing the song"
            }

    # Method to retrieve all songs of the user in order of their positions.
    def show_songs_order(self):
        try:
            # Querying all songs of the user and ordering them by their positions.
            songs = session.query(Songs).filter_by(user_id=self.user_id).order_by(Songs.order.desc()).all()
            for song in songs:
                music_info = str(song.id) + '.' + ' Name: ' + str(song.name)
                if song.order:
                    music_info += ' | Position: ' + str(song.order)
                else:
                    music_info += ' | Position: Not set'

                print(music_info)  # Printing information about each song

                return {
                        "success": True,
                        "message": "Successfully showed the songs"
                    }
        except SQLAlchemyError as e:
            logging.exception("Error showing songs order")
            return {
                    "success": False,
                    "message": "No songs to show"
                }

    # Method to update the position of a song in the user's playlist.
    def update_songs_order(self, song_id, order):
        try:
            song = session.query(Songs).filter_by(id=song_id, user_id=self.user_id).first()
            if song is not None:
                song.order = order  # Updating the position of the song.
                session.commit()  # Committing the transaction.
                return {
                    "success": True,
                    "message": "Position updated successfully"
                }
            else:
                return {
                    "success": False,
                    "message": "Song not found"
                }

        except SQLAlchemyError as e:
            logging.exception("Error updating songs order")  # Logging exception if error occurs.
            return {
                "success": False,
                "message": "An error occurred while updating the song"
            }

    # Method to show existing songs
    def show_songs(self):
        try:
            # Querying all songs of the user and ordering them by their positions.
            songs = session.query(Songs).filter_by(user_id=self.user_id).order_by(Songs.order.desc()).all()
            key = 1

            print('\n')
            for song in songs:
                music_info = str(key) + '.' + ' Name: ' + str(song.name)
                if song.artist:
                    music_info += ' | Artist: ' + str(song.artist)
                if song.album:
                    music_info += ' | Album: ' + str(song.album)
                if song.duration:
                    music_info += ' | Duration: ' + str(song.duration)

                key += 1

                print(music_info)  # Printing information about each song.

            return {
                "success": True,
                "message": "Successfully showed the songs"
            }
        except SQLAlchemyError as e:
            logging.exception("Error showing songs")  # Logging exception if error occurs.
            return {
                "success": False,
                "message": "No songs to show"
            }