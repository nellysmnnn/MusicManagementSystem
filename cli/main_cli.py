from cli.cli_inputs import CLIInputs
from songs.genres_crud import GenresCrud
from songs.playlist_crud import PlaylistCrud
from songs.search import Search
from songs.songs_crud import SongsCrud


# Class for users to be able to perform operations such as adding, editing, and deleting recipes via the
# command line.
class MainCLI(CLIInputs):
    def __init__(self, user_id):
        self.user_id = user_id

    # Creating method for the main menu actions
    def main_menu(self):
        print("\n")
        print("0. Exit")
        print("1. Songs")
        print("2. Playlists")
        print("3. Genres")
        print("4. Search")
        action = self.input_option()

        # Quitting the program
        if action == 0:
            self.quit()
        # Displaying playlist actions
        elif action == 2:
            self.playlist_actions()
        # Displaying song actions
        elif action == 1:
            self.song_actions()
        # Displaying genre actions
        elif action == 3:
            self.genre_actions()
        # Handling user search
        elif action == 4:
            self.search()

    # Method for interacting with playlists
    def playlist_actions(self):
        print("\n")
        # Playlist interaction options
        print("0. Main menu")
        print("1. Add playlist")
        print("2. Remove playlist")
        print("3. Show all playlists")
        print("4. Change playlist")
        action = self.input_option()
        # Returning back to main menu
        if action == 0:
            self.main_menu()
        # Adding new playlist
        if action == 1:
            self.add_playlist()
        # Removing a playlist
        if action == 2:
            self.remove_playlist()
        # Showing existing playlists
        if action == 3:
            self.show_playlists()
        # Changing a playlist
        if action == 4:
            self.change_playlist()

    # Method for adding a new playlist
    def add_playlist(self):
        # Getting the name of new playlist from user
        playlist_name = input("Enter playlist name: ")
        # Adding the playlist
        adding = PlaylistCrud(self.user_id).add_playlist(playlist_name)
        print(adding['message'])
        # Returning back to main menu
        self.main_menu()

    # Method for removing a playlist
    def remove_playlist(self):
        # Getting the name of removing playlist from user
        playlist_name = input("Enter playlist name: ")
        # Removing the playlist
        removing = PlaylistCrud(self.user_id).remove_playlist(playlist_name)
        print(removing['message'])
        # Returning back to main menu
        self.main_menu()

    # Method for changing a playlist
    def change_playlist(self):
        # Getting the name of changing playlist and its new name from the user
        playlist_name = input("Enter playlist name you want to change: ")
        new_name = input("Enter new playlist name: ")
        # Changing the playlist name
        changing = PlaylistCrud(self.user_id).change_playlist(playlist_name, new_name)
        print(changing['message'])
        # Returning back to main menu
        self.main_menu()

    # Method for showing the existing playlists
    def show_playlists(self):
        # Trying to get the playlists from our database
        showing_playlists = PlaylistCrud(self.user_id).show_playlists()
        # Showing playlists if found
        if showing_playlists['data']:
            for (playlist_id, playlist_name) in showing_playlists['data'].items():
                print(str(playlist_id) + '.', playlist_name)
        else:
            print("No playlists")

        if not showing_playlists['success']:
            print(showing_playlists['message'])

        # Returning back to main menu
        self.main_menu()

    # Method for interacting with songs
    def song_actions(self):
        # Displaying song interaction options
        print("\n")
        print("0. Main menu")
        print("1. Add song")
        print("2. Remove song")
        print("3. Show songs")
        print("4. Reorder songs")
        action = self.input_option()

        # Returning back to main menu
        if action == 0:
            self.main_menu()
        # Adding a song
        elif action == 1:
            self.add_song()
        # Removing a song
        elif action == 2:
            self.remove_song()
        # Showing the songs
        elif action == 3:
            self.show_songs()
        # Reordering the songs
        elif action == 4:
            self.reorder_songs()
        else:
            print("Please enter a valid number")
            # In case fo an invalid input returning back to song interaction options
            self.song_actions()

    # method for adding a new song
    def add_song(self):
        playlist_id = None
        genre_id = None
        # Getting data from the user for the song they want to add
        song_name = input("Enter song name: ")
        song_artist = input("Enter song artist: ")
        song_album = input("Enter song album: ")
        song_duration = input("Enter song duration: ")

        # Getting existing genres to display them
        geners = GenresCrud().get_genres()
        # Checking if there are any genres
        if geners['data']:
            print('\nGenres found: ')
            # Iterating through the genres dict to display genres information
            for (genre_id, genre_name) in geners['data'].items():
                print(str(genre_id) + '.', genre_name)
            checking_flag_1 = True
            while checking_flag_1:
                genre_id = self.input_option("Choose a genre number from list above: ")
                checking_flag_1 = False
                # Making sure there is a genre in that dict with inputted name
                if genre_id not in list(geners['data'].keys()):
                    print('Please enter a valid number')
                    checking_flag_1 = True

        # Getting existing playlists to display them
        playlists = PlaylistCrud(self.user_id).show_playlists()
        # Checking if there are any playlists
        if playlists['data']:
            print('\nPlaylists found:')
            # Iterating through the playlists dict to display the playlists information
            for (playlist_id, playlist_name) in playlists['data'].items():
                print(str(playlist_id) + '.', playlist_name)
            checking_flag_2 = True
            while checking_flag_2:
                playlist_id = self.input_option("Choose a playlist number from list above: ")
                checking_flag_2 = False
                # Making sure there is a playlist in that dict with inputted name
                if playlist_id not in list(playlists['data'].keys()):
                    print('Please enter a valid number')
                    checking_flag_2 = True
        # Adding a song with all the inputted features
        adding = SongsCrud(self.user_id).add_song({
            'song_name': song_name,
            'song_artist': song_artist,
            'song_album': song_album,
            'song_duration': song_duration,
            'genre_id': genre_id,
            'playlist_id': playlist_id
        })

        print(adding['message'])
        # Returning back to song interaction options
        self.song_actions()

    # Method for removing a song
    def remove_song(self):
        # Getting the name of the song user wants to remove
        song_name = input("Enter song name: ")
        # Removing the song
        removing = SongsCrud(self.user_id).remove_song(song_name)
        print(removing['message'])
        # Returning back to main menu
        self.song_actions()

    # Method for reordering the songs
    def reorder_songs(self):
        # Displaying the current songs order
        SongsCrud(self.user_id).show_songs_order()
        # Getting number of the song the user wants to be reordered
        song_id = self.input_option('Choose song number:')
        # Getting new position of the song from user
        order_number = self.input_option('Set order number (the higher the number the higher):')
        # Updating songs order
        update = SongsCrud(self.user_id).update_songs_order(song_id, order_number)
        print('\n' + update['message'] + '\n')
        # Returning back to song interaction options
        self.song_actions()

    # Method for showing the existing songs
    def show_songs(self):
        SongsCrud(self.user_id).show_songs()
        self.song_actions()

    # Method for genres interacting options
    def genre_actions(self):
        # Displaying genres interacting options
        print('\n')
        print("0. Main menu")
        print("1. List all genres")
        print("2. Add a genre")
        action = self.input_option()

        # Returning back to main menu
        if action == 0:
            self.main_menu()
        # Showing existing genres
        if action == 1:
            self.show_genres()
        # Adding a new genre
        if action == 2:
            self.add_genres()

    # Method for showing existing genres
    def show_genres(self):
        # Trying to get the existing genres from our database
        geners = GenresCrud().get_genres()
        if geners['success']:
            # Making sure there are any genres in the genres dict
            if geners['data']:
                # Displaying the existing genres
                for (genre_id, genre_name) in geners['data'].items():
                    print(str(genre_id) + '.', genre_name)
            else:
                print("No genres")
        else:
            print(geners['message'])

        # Returning back to genre interaction options
        self.genre_actions()

    # Method for adding a new genre
    def add_genres(self):
        # Getting the name of the new genre
        genre_name = input("Enter genre name: ")
        # Adding new genre
        response = GenresCrud().add_genre(genre_name)

        print(response['message'])

        # Returning back to genres interaction options
        self.genre_actions()

    # Method for search feature that allows users to search for
    # specific songs or playlists based on keywords
    def search(self):
        # Getting the keyword from the user
        keyword = input("Enter the keyword: ")
        Search().search(keyword)
        # Returning back to main menu
        self.main_menu()
