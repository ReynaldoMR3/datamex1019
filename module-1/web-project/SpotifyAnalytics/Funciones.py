import pandas as pd
import numpy as np
import json
from json.decoder import JSONDecodeError
from pandas.io.json import json_normalize
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.oauth2 as oauth2
import spotipy.util as util
import spotipy
#Cargamos el archivo track_elements.json para poder utilizarlo posteriormente
data = pd.read_json('tracks_elements.json', orient='records')

# Se acomoda la tabla basada en popularity
data = data.sort_values(by=['popularity'], ascending=False)

#Obtenemos las 100 canciones mas populares dentro del df y las copiamos a un nuevo df.
top_100 = data[0:100].copy()

#funciones para limpiar la base de datos.
#Eliminando columnas que no me interesan
top_100_clean = top_100.drop(columns=['album', 'available_markets', 'disc_number', 'explicit', 'external_ids',
                                'external_urls', 'href', 'is_local', 'preview_url', 'track_number', 'type']).copy()

#list comprehension que obtiene los nombres de la columna artists
top_100_clean['artists'] = [[i['name'] for i in e] for e in top_100_clean['artists']]

#Abriendo la base de datos de kaggle con un data frame
top_2018 = pd.read_csv('top2018.csv')

#añadiendo la columna year
top_2018['year'] = 2018

#Revisando que columnas contiene la base de datos.
#print(top_2018.columns)
#print('')
#print(top_100_clean.columns)


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


# Función que sirve como print de json para verlos de una manera mas clara
def clear_json(var):
    return print(json.dumps(var, sort_keys=True, indent=4))

# Funcion que obtiene los track features de la columna ids del data frame top_100_clean
def get_tracks_features(var):
    return spotify.audio_features(tracks=[i for i in var])

tracks_features = get_tracks_features(top_100_clean['id'])

#convirtiendo el json a dataframe
tracks_featuresdf = pd.DataFrame(tracks_features)

#uniendo los dataframes
frames = [tracks_featuresdf, top_100_clean]
finaldf = pd.merge(tracks_featuresdf, top_100_clean, how='right')

#Acomodando y eliminando columnas del findaldf para que sean iguales a las columnas del database
finaldf = finaldf[['id', 'name', 'artists', 'danceability', 'energy', 'key',
                   'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness',
                   'liveness', 'valence', 'tempo', 'duration_ms', 'time_signature']]

finaldf['year'] = 2019

#Haciendo un append al database del 2018 con el df finaldf con tracks del 2019
finaldb = top_2018.append(finaldf)

#Convirtiendo el dataframe a excel
finaldb.to_excel('toptracks2018y2019.xlsx')
