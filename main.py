import spotipy
from spotipy.oauth2 import SpotifyOAuth
from ID import *
import json

#initial setup
SCOPE = 'playlist-modify-public'
spotifyOBJ = SpotifyOAuth(client_id = CLIENT_ID, client_secret = CLIENT_ID_SECRET, redirect_uri = REDIRECT, scope = SCOPE, username = USER)
spotify = spotipy.Spotify(auth_manager = spotifyOBJ)

#inputs
#playlistName = input("Name of playlist")
#playlistDesc = input("Description of playlist")
genresJSON = spotify.recommendation_genre_seeds()
genres = genresJSON['genres']


for i in range(len(genres)):
    index = i + 1
    print(index,". " , genres[i])

targetGenre = input("Please select # to explore genre")
targetGenre = int(targetGenre) - 1
numTracks = input("Number of tracks")
numTracks = int(numTracks)


recommendations = spotify.recommendations(seed_genres = [genres[targetGenre]] , limit = numTracks)

#playlist create
playlistName = genres[targetGenre] + "exploration"
playlistDesc = "Playlist of all " + genres[targetGenre] + " songs."

spotify.user_playlist_create(user = USER, name = playlistName, public = True, description = playlistDesc)

#grab newPlaylist as newest playlist created
playlists = spotify.user_playlists(user = USER)
newPlaylist = playlists['items'][0]['id']

#print(recommendations["tracks"][0]["uri"])
tracklist = []
for i in range(numTracks):
    tracklist.append(recommendations['tracks'][i]['uri'])

print(tracklist)
    
spotify.user_playlist_add_tracks(user = USER,playlist_id = newPlaylist,tracks = tracklist)



