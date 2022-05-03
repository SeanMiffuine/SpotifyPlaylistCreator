import spotipy
from spotipy.oauth2 import SpotifyOAuth
from ID import *
import json

SCOPE = 'playlist-modify-public'
spotifyOBJ = SpotifyOAuth(client_id = CLIENT_ID, client_secret = CLIENT_ID_SECRET, redirect_uri = REDIRECT, scope = SCOPE, username = USER)
spotify = spotipy.Spotify(auth_manager = spotifyOBJ)

playlistName = input("Name of playlist")
playlistDesc = input("Description of playlist")

spotify.user_playlist_create(user = USER, name = playlistName, public = True, description = playlistDesc)

song = input('Enter Song')

search = spotify.search(q = song)

songs = []

songs.append(search['tracks']['items'][0]['uri'])

playlists = spotify.user_playlists(user = USER)
newPlaylist = playlists['items'][0]['id']

spotify.user_playlist_add_tracks(user = USER,playlist_id = newPlaylist,tracks = songs)



