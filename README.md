# Maestro - Music Recommendation Engine

## Introduction

This program is a network based recommendation system that evaluates artists and music on a variety of criteria, including song similarity and overall artist similarity. It does so by making comparisons between artists with information such as genre overlap, and takes a deeper dive into their songs to measure overlap in things such as mood or energy. 

Maestro is one component of a project for [GEICO Hacktivates 2019](https://www.geico.com/geicohacktivates/). My team created a chatbot focused on music recommendation & playback. 

Alongside Trevor Cunningham, Aidan Miller, and Adam Ratzmann, I represented Indiana University - Bloomington against the University of Maryland - College Park in the semi-final round. 

We will be representing IU again on November 8th against the University of California - Riverside in the final round. The full repository for the first leg of the team's project can be found over at [Adam Ratzmann's Github.](https://github.com/adamint/geico-hackathon-kotlin)

___

## Details

My method for music recommendation is built by forming a network of artists, and then creating links between them with associated weights. The weights' values are the 'artist similarity score'. 

This is determined by generating 

- their shared genre score  — measures the % of shared genres between artists
- top songs similarity score — measures the similarity of both artists top 10 songs 

I've used Spotipy for acquiring music data from [Spotify's API](https://developer.spotify.com). In order to build networks of musicians with that data, I've used [NetworkX](https://networkx.github.io).

---

## How to Run This Program

#### Packages

You'll need to install the aforementioned packages, NetworkX and Spotipy 

`pip install networkx`

`pip install spotipy`

#### Credentials

Afterwards, you'll need to pop over to [Spotify's Developer Dashboard](https://developer.spotify.com/dashboard/) and grab a `Client ID` and `Client Secret`.

Once you've done that, go ahead and create a file called `apiKeys.py`, and add:

`spotifySecret = 'Your_Secret_Key'`

Save the file.

In the `spotifyData.py` file, replace the `client_id` value in the `credentials` variable with your Client ID from Spotify. 

#### Interacting with Spotify Data

*Coming Soon!*

#### Generating Artist Networks

*Coming Soon!*


---
