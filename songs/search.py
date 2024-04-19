import sqlalchemy
from sqlalchemy import or_

from db.db_connection import Songs, session, Genres, Playlists

# Class for handling user search feature that allows users to search for
# specific songs or playlists based on keywords
class Search:
    def search(self, keyword):
        # Formatting the keyword for SQL LIKE clause.
        search = "%{}%".format(keyword)
        # Querying songs with outer joins to include related genres and playlists.
        songs = (session.query(Songs).outerjoin(Songs.genre).outerjoin(Songs.playlist)
                 .filter(or_(Songs.name.like(search),
                             Songs.artist.like(search),
                             Genres.name.like(search),
                             Playlists.name.like(search))).order_by(Songs.order.desc()).all())

        # Iterating through songs found according to search and displaying songs data
        for song in songs:
            print('\n')
            print(f'Music name:  {song.name}')
            if song.artist:
                print(f'Artist:  {song.artist}')
            if song.album:
                print(f'Album: {song.album}')
            if song.duration:
                print(f'Duration:  {song.duration}')
            if song.genre:
                print(f'Genre:  {song.genre.name}')
            if song.playlist:
                print(f'Playlist:  {song.playlist.name}')
