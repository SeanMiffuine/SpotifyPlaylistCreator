import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from ID import *
import json


titleScreen = """
====================================

    SPOTIFY NEW MUSIC EXPLORER:
        create playlsts with
        undiscovered music !


            by Sean Tang

====================================
"""
#initial setup for spotify object
SCOPE = 'playlist-modify-public'
spotifyOBJ = SpotifyOAuth(client_id = CLIENT_ID, client_secret = CLIENT_ID_SECRET, redirect_uri = REDIRECT, scope = SCOPE, username = USER)
spotify = spotipy.Spotify(auth_manager = spotifyOBJ)
genresJSON = spotify.recommendation_genre_seeds()
genres = genresJSON['genres']

    
class PlaylistGenerator:


    def __init__(self):
        #initialize values
        self.targetGenre = 0
        self.numTracks = 0
        self.recommendations = []
        self.newPlaylist = ''
        self.tracklist = []
        
    def getInputs(self):
        #get data about playlist to generate
        self.targetGenre = input("Please select # to explore genre: ")
        self.targetGenre = int(self.targetGenre) - 1
        self.numTracks = int(input("Number of tracks within playlist(1 - 100): "))
        self.numTracks = int(self.numTracks)

    def showGenres(self):
        for i in range(len(genres)):
            index = i + 1
            print(index,". " , genres[i])

    def getRecommendations(self):
        #generates number of recommended tracks
        print(self.targetGenre)
        self.recommendations = spotify.recommendations(seed_genres = [genres[self.targetGenre], genres[self.targetGenre + 1]] , limit = self.numTracks)

    def makePlaylist(self):
        #makes new playlist
        playlistName = genres[self.targetGenre] + " exploration"
        playlistDesc = "Playlist of undiscovered " + genres[self.targetGenre] + " songs."

        spotify.user_playlist_create(user = USER, name = playlistName, public = True, description = playlistDesc)
        playlists = spotify.user_playlists(user = USER)
        self.newPlaylist = playlists['items'][0]['id']

    def addTracks(self):
        for i in range(self.numTracks):
            self.tracklist.append(self.recommendations['tracks'][i]['uri'])

        spotify.user_playlist_add_tracks(user = USER, playlist_id = self.newPlaylist, tracks = self.tracklist)

    def reset(self):
        self.targetGenre = 0
        self.numTracks = 0
        self.recommendations = []
        self.newPlaylist = ''
        self.tracklist = []
            
def main():
    generator = PlaylistGenerator()
    input(titleScreen)
    os.system('cls')
    
    while True:
        generator.showGenres()
        generator.getInputs()
        generator.getRecommendations()
        generator.makePlaylist()
        generator.addTracks()
        generator.reset()

if __name__ == "__main__":
    main()
