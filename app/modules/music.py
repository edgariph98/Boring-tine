

import spotipy
import json
import random
from .config import spotifyCredentials
from spotipy.oauth2 import SpotifyClientCredentials
CLIENT_ID = spotifyCredentials["Client"]
CLIENT_SECRET = spotifyCredentials["Secret"]
client_credentials_manager = SpotifyClientCredentials(CLIENT_ID, CLIENT_SECRET) # Remember to export id and secret
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def song_search(user_input): #--> generates 5 random songs based on arbitrary user input
    objects = [{"artist":"", "title":"", "uri":""}, {"artist":"", "title":"", "uri":""}, {"artist":"", "title":"", "uri":""}, {"artist":"", "title":"", "uri":""}, {"artist":"", "title":"", "uri":""}]
    query = user_input + " " + random_search()
    results = sp.search(query, limit=5)
    items = results['tracks']['items']
    for i in range(0, 5):
        objects[i]["artist"] = items[i]["artists"][0]["name"]
        objects[i]["title"] = items[i]["name"]
        objects[i]["uri"] = items[i]["uri"][14:]

    return objects
    
def songs_genre_based(genre_chosen,n):# --> returns random 3 songs based on genre_chosen
    # objects = [{"artist":"", "title":"", "uri":""}, {"artist":"", "title":"", "uri":""}, {"artist":"", "title":"", "uri":""}]
    objects = []
    query = random_search() + " genre:" + genre_chosen
    results = sp.search(query, limit=n)
    items = results['tracks']['items']
    i = 0
    for i in range(0, n):
        songObject ={}
        songObject["artist"] = items[i]["artists"][0]["name"]
        songObject["title"] = items[i]["name"]
        songObject["uri"] = items[i]["uri"][14:]
        songObject["genre"] = genre_chosen
        objects.append(songObject)
        i = i+1
        # objects[i]["artist"] = items[i]["artists"][0]["name"]
        # objects[i]["title"] = items[i]["name"]
        # objects[i]["uri"] = items[i]["uri"][14:]

    return objects

def getAllSongs(genres, n):
    songs = []
    for genre in genres:
        songs = songs + songs_genre_based(genre,n)

    return songs
def random_search():
    characters = "abcdefghijklmnopqrstuvwxyz"
    randomCharacter = characters[random.randint(0, 25)]
    return randomCharacter

if __name__ == "__main__":
    print(json.dumps(getAllSongs(["Alternative Rock","Pop"],2),indent=1))