# Run in python3
import sys
import spotifyData as spotify
import networkx as nx
import matplotlib.pyplot as plt

# Must pass argument as string

#artistName = sys.argv[1]
#print(artistName)

# Related Artist params: name, id, genres, followers->total, images, popularity

# Use related artists to make a network -- returns a Graph/Network
def makeArtistNetwork(artistID):
    
    artist = spotify.artistDataID(artistID)
    related = spotify.getRelatedArtists(artistID)['artists']
    # print(related)
    
    # Create graph
    G = nx.Graph()
    # Add main artist node
    G.add_node(artist['name'], id=artist['id'], genres=artist['genres'], followers=artist['followers']['total'], popularity=artist['popularity'])
    
    # Add related artist nodes to graph
    for a in related:
        G.add_node(a['name'], id=a['id'], genres=a['genres'], followers=a['followers']['total'], popularity=a['popularity'])
        
        # Add edge between main artist and secondary - main artist hub
        G.add_edge(str(artist['name']), str(a['name']))
        G[artist['name']][a['name']]['weight'] = artistSimilarityScore(artist['id'], a['id'])    
    
    return G

# Score of similar genres between artists
def genreScore(artist1ID, artist2ID):
    
    count = 0
    artist1Genres = spotify.artistDataID(artist1ID)['genres']
    artist2Genres = spotify.artistDataID(artist2ID)['genres']

    for g in artist1Genres:
        if g in artist2Genres:
            count += 1

    pct = count / len(artist1Genres)
    return pct

# Calculate similarity of 2 artists top songs -> then add to edge weight as topSongSimilarity
def topSongScore(artistID1, artistID2):


    topSongs1 = [ track['id'] for track in spotify.getTopTracks(artistID1)['tracks'] ]
    topSongs2 = [ track['id'] for track in spotify.getTopTracks(artistID2)['tracks'] ]
    
    score = 0

    for i in topSongs1:
        for j in topSongs2:
            score += songSimilarity(i, j)
    
    # print('Similarity Score for top songs by', spotify.getArtistName(artistID1), '&', spotify.getArtistName(artistID2), ":", score/100)
    return score/100

# Calculate song similarity number based on valence, mode, and energy
def songSimilarity(song1ID, song2ID):

    song1Features = spotify.getAudioFeatures(song1ID)
    song2Features = spotify.getAudioFeatures(song2ID)

    valenceScore = 1 - (abs(song1Features[0]['valence'] - song2Features[0]['valence']))
    energyScore = 1 - (abs(song1Features[0]['energy'] - song2Features[0]['energy']))
    danceScore = 1 - (abs(song1Features[0]['danceability'] - song2Features[0]['danceability']))
    
    if (song1Features[0]['mode'] == song2Features[0]['mode']):
        mode = 1
    else:
        mode = 0

    # print('ValenceScore:', valenceScore, 'Mode:', mode, 'EnergyScore:', energyScore, 'danceScore:', danceScore)

    score = (valenceScore + energyScore + mode + danceScore) / 4
    
    return score

def artistSimilarityScore(artist1ID, artist2ID):
    genre = genreScore(artist1ID, artist2ID)
    topSongs = topSongScore(artist1ID, artist2ID)
    score = (genre + topSongs) / 2
    # print('Artist similarity score between', spotify.getArtistName(artist1ID), '&', spotify.getArtistName(artist2ID), ':', score)
    return score 

# Pass in an artist node from a built graph (that has similarity calculated) and returns an artist as a String
def recommendArtist(graph, artistName):
    scores = {}
    for nbr in graph[artistName]:
        #print(nbr)
        scores[graph[artistName][nbr]['weight']] = (artistName, nbr)
    #print(scores)
    #print(max(scores.keys()))
    artistRec = scores[max(scores.keys())][1]
    #print(scores[max(scores.keys())])
    return artistRec


