from sqlalchemy.exc import SQLAlchemyError
from db.db_connection import *

# Class for CRUD operations with the genres
class GenresCrud:

    # Method to add a new genre to the database
    def add_genre(self, genre_name):
        try:
            # Creating a new Genres object with the given name.
            genre_to_add = Genres(name=genre_name)
            # Adding the new genre to the session and committing
            session.add(genre_to_add)
            session.commit()
            return {
                'success': True,
                'message': 'Successfully added genre'
            }
        except SQLAlchemyError as e:
            # Logging exception if error occurs.
            logging.exception("Error adding genre")
            return {
                'success': False,
                'message': 'An error occurred while adding genre'
            }

    # Method for getting the existing genres
    def get_genres(self):
        try:
            # Creating a dict to store genres data
            genres_dict = {}
            # Querying genres from our database
            genres = session.query(Genres).all()

            # Iterating through genres and storing genres data to our dict
            for genre in genres:
                genres_dict[genre.id] = genre.name

            # Returning genres dict
            return {
                'success': True,
                'message': '',
                'data': genres_dict
            }
        except SQLAlchemyError as e:
            # Logging exception if error occurs.
            logging.exception("Error getting genres")
            return {
                'success': False,
                'message': 'An error occurred while showing genres'
            }
