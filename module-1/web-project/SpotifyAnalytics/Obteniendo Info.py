import spotipy
import os
import sys
import webbrowser
import pandas as pd
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.oauth2 as oauth2
import spotipy.util as util
import json
from json.decoder import JSONDecodeError
import requests
import numpy as np
#user iD: 1291997954
'''
Este archivo sirve para obtener información de la api de spotify y convertirla a
un json para poder utilizar la información en otro archivo
'''
# Autoriza la api de spotify
with open('client.txt') as f:
    client_id = f.readlines()
    client_id = client_id[0].split()
    client_id = client_id[0]

with open('secret.txt') as s:
    secret_id = s.readlines()
    secret_id = secret_id[0]

token = util.oauth2.SpotifyClientCredentials(client_id=client_id, client_secret=secret_id)
cache_token = token.get_access_token()
spotify = spotipy.Spotify(cache_token)

# Cargando la base de datos del top 100 canciones en el 2018
db_csv = 'top2018.csv'


def open_csv(csv):
    return pd.read_csv(csv, sep=',')


df = open_csv(db_csv)


# Función que sirve como print de json para verlos de una manera mas clara
def clear_json(var):
    return print(json.dumps(var, sort_keys=True, indent=4))


# Función que sirve para buscar las listas de 10 playlists que contentan top 100 tracks 2019.

def buscando_playlists(string):
    return spotify.search(q=string, limit=10, type='playlist')


busca = buscando_playlists('top 100 tracks 2019')


#funcion que saca los ids de las playlists en la variable busca
def obten_playlist_id(var):
    playlists= var['playlists']
    substract_id = 'id'
    playlists_id = [i['id'] for i in playlists['items'][0:] if substract_id in i]
    user_play =playlists['items'][0:]
    user_id1 = [i['owner'] for i in user_play]
    user_id = [i['id'] for i in user_id1]
    return playlists_id, user_id

lista_ids =obten_playlist_id(busca)

lista_usersids= lista_ids[1]
lista_playlistid = lista_ids[0]

#Creando listas para pordre guardar las tracks que contiene cada una de las playlists.
playlist_1 = spotify.user_playlist(lista_usersids[0], lista_playlistid[0])
playlist_2 = spotify.user_playlist(lista_usersids[1], lista_playlistid[1])
playlist_3 = spotify.user_playlist(lista_usersids[2], lista_playlistid[2])
playlist_4 = spotify.user_playlist(lista_usersids[3], lista_playlistid[3])
playlist_5 = spotify.user_playlist(lista_usersids[4], lista_playlistid[4])
playlist_6 = spotify.user_playlist(lista_usersids[5], lista_playlistid[5])
playlist_7 = spotify.user_playlist(lista_usersids[6], lista_playlistid[6])
playlist_8 = spotify.user_playlist(lista_usersids[7], lista_playlistid[7])
playlist_9 = spotify.user_playlist(lista_usersids[8], lista_playlistid[8])
playlist_10 = spotify.user_playlist(lista_usersids[9], lista_playlistid[9])

#clear_json(playlist_1['tracks']['items'][0]['track']['uri'])

#Función que nos permite obtener los uri tracks de las playlists
def get_tracks_uris(playlist):
    substract_uri = 'uri'
    get_tracks = playlist['tracks']
    get_items = get_tracks['items']
    get_uris = [i['track']['uri'] for i in get_items]
    return get_uris

#Usando la función para obtener las listas con los uris y uniendolas en una sola lista.
uri_playlist1 = get_tracks_uris(playlist_1)
uri_playlist2 = get_tracks_uris(playlist_2)
uri_playlist3 = get_tracks_uris(playlist_3)
uri_playlist4 = get_tracks_uris(playlist_4)
uri_playlist5 = get_tracks_uris(playlist_5)
uri_playlist6 = get_tracks_uris(playlist_6)
uri_playlist7 = get_tracks_uris(playlist_7)
uri_playlist8 = get_tracks_uris(playlist_8)
uri_playlist9 = get_tracks_uris(playlist_9)
uri_playlist10 = get_tracks_uris(playlist_10)

#concatenando las listas y uniendolas para obtener el track id y obteniendo un array con uris unicas
uri_tracks = uri_playlist1 + uri_playlist2 + uri_playlist3 + uri_playlist4 + uri_playlist5 + uri_playlist6 + uri_playlist7 + uri_playlist8 + uri_playlist9 + uri_playlist10
clean_uris = [i.split(':')[2] for i in uri_tracks]
unique_uris = np.array(clean_uris)
unique_uris = np.unique(unique_uris)

#obteniendo la lista de tracks con los tracks ids:
def lista_tracks(var):
    tracks= []
    for i in var:
        tracks.append(spotify.track(i))
    return tracks

track_elements = lista_tracks(unique_uris)

with open ('tracks_elements.json', 'w') as json_file:
    json.dump(track_elements, json_file)
