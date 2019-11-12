import pandas as pd
import numpy as np
import json
from json.decoder import JSONDecodeError
from pandas.io.json import json_normalize

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
print(top_2018.columns)
print('')
print(top_100_clean.columns)
