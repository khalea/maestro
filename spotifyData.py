from apiKeys import spotifySecret # Spotify Secret Key
import spotipy as sp
import spotipy.oauth2 as oauth2

# Spotify Authorizations
credentials = oauth2.SpotifyClientCredentials(
        client_id='fe7124f2090f42d08020787c0fef54cf',
        client_secret=spotifySecret)

token = credentials.get_access_token()
spotify = sp.Spotify(auth=token)


# Grab data for a single artist by text/name
def artistDataName(artist):
    # Grab raw JSON data
    rawData = spotify.search(q=artist, limit=1, offset=0, type='artist')
    # Filters down to first artist's data
    artist = rawData['artists']['items'][0]
    return artist

# Grab data for a single artist by ID
def artistDataID(artistID):
    # Grab raw JSON data
    rawData = spotify.artist(artistID)
    # Filters down to first artist's data
    # artist = rawData['artists']['items'][0]
    return rawData

def getArtistName(artistID):
    name = spotify.artist(artistID)['name']
    return name


# Grab Related from Spotify -- Returns 20 artists
def getRelatedArtists(artistID):
    related = spotify.artist_related_artists(artistID)
    return related

def getTopTracks(artistID):
    top = spotify.artist_top_tracks(artistID)
    return top

def getAudioFeatures(song1ID):
    songFeatures = spotify.audio_features([song1ID])
    return songFeatures

def getSongName(songID):
    data  = spotify.track(songID)
    return data['name']

def getArtistGenres(artistID):
    genres = artistDataID(artistID)['genres']
    return genres

def getArtistID(artistName):
    return artistDataName(artistName)['id']
