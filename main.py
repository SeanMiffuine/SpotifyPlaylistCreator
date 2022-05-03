import spotipy
from spotipy.oauth2 import SpotifyOAuth
from ID import *
import json

#initial setup
SCOPE = 'playlist-modify-public'
spotifyOBJ = SpotifyOAuth(client_id = CLIENT_ID, client_secret = CLIENT_ID_SECRET, redirect_uri = REDIRECT, scope = SCOPE, username = USER)
spotify = spotipy.Spotify(auth_manager = spotifyOBJ)

#inputs
playlistName = input("Name of playlist")
playlistDesc = input("Description of playlist")

#playlist create
spotify.user_playlist_create(user = USER, name = playlistName, public = True, description = playlistDesc)

#grab newPlaylist as newest playlist created
playlists = spotify.user_playlists(user = USER)
newPlaylist = playlists['items'][0]['id']






song = input('Enter Song')

search = spotify.search(q = song)

songs = []

songs.append(search['tracks']['items'][0]['uri'])
spotify.user_playlist_add_tracks(user = USER,playlist_id = newPlaylist,tracks = songs)



