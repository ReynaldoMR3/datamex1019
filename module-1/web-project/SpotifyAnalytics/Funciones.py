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

#Función que obtiene los nombres de la columna artists
def get_artist_name(df):
    df['artists'] = [i.get('name') for i in df['artists'][0]]
    return df

top_100_clean = get_artist_name(top_100_clean)

print(top_100_clean[['artists','name','popularity']])
