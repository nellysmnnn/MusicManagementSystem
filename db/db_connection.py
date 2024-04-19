import os

import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine
import logging

logging.disable(logging.INFO)  # Disabling logging for info messages.
Base = sqlalchemy.orm.declarative_base()  # Creating base class for ORM models.
db_path = os.path.join(os.path.dirname(__file__), 'app.db')  # Constructing path to the database file.
db_uri = 'sqlite:///{}'.format(db_path)  # Creating database URI for SQLite.
engine = create_engine(db_uri, echo=True)  # Creating SQLAlchemy engine for database interaction with echo enabled for logging SQL statements.
connection = engine.connect()  # Establishing connection to the database.
Session = sessionmaker(bind=engine)  # Creating session class bound to the engine.
session = Session()  # Creating session object for interacting with the database.

# Defining SQLAlchemy ORM models for tables in the database.
# Create Users table model
class Users(Base):
    __tablename__ = 'users'  # Table name
    id = Column(Integer, primary_key=True)  # Primary key column
    email = Column(String, nullable=False, unique=True)  # Column for user email
    password = Column(String, nullable=False)  # Column for user password

# Create Playlists table model
class Playlists(Base):
    __tablename__ = 'playlist'  # Table name
    id = Column(Integer, primary_key=True)  # Primary key column
    name = Column(String)  # Column for storing playlist name
    user_id = Column(Integer, ForeignKey('users.id'))  # Foreign key column referencing the user who owns the playlist
    songs = relationship("Songs", back_populates="playlist")  # Relationship to the Songs table

# Create Songs table model
class Songs(Base):
    __tablename__ = 'songs'  # Table name
    id = Column(Integer, primary_key=True)  # Primary key column
    name = Column(String)  # Column for song name
    artist = Column(String, nullable=True)  # Column for artist name
    album = Column(String, nullable=True)  # Column for album name
    duration = Column(String, nullable=True)  # Column for song duration
    order = Column(Integer, nullable=True)  # Column for song order
    genre_id = Column(Integer, ForeignKey('genres.id'), nullable=True)  # Foreign key column referencing the genre of the song
    user_id = Column(Integer, ForeignKey('users.id'))  # Foreign key column referencing the user who owns the song
    playlist_id = Column(Integer, ForeignKey('playlist.id'), nullable=True)  # Foreign key column referencing the playlist the song belongs to
    genre = relationship("Genres", back_populates="songs", uselist=False)  # Relationship to the Genres table
    playlist = relationship("Playlists", back_populates="songs", uselist=False)  # Relationship to the Playlists table

# Create Genres table model
class Genres(Base):
    __tablename__ = 'genres'  # Table name
    id = Column(Integer, primary_key=True)  # Primary key column
    name = Column(String, nullable=False)  # Column for genre name
    songs = relationship("Songs", back_populates="genre")  # Relationship to the Songs table


Base.metadata.create_all(engine)  # Creating all tables defined by Base in the database.






