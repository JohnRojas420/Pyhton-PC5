# Descargar un archivo .zip mediante código del siguiente url (https://netsg.cs.sfu.ca/youtubedata/) 
# (recomiendo descargar el archivo 0333.zip que es menos pesado)
# Descomprimir los datos en una carpeta que genere y leer mediante pandas alguno de los archivos en esta. 
# (observar que no es necesario en un primer momento leer los datos con un nombre de columna especifico)
# Los nombres de columna pueden ser puestos posteriormente
# El separador de columna es \t
# Se colocan los nombres de columnas y descripción asociada para su intermetación. 
# Ejemplo columna1 sera VideoID ...
# Procesar los datos según:
# Nos quedaremos con las columnas: VideoID, edad, catgoria, views, rate.
# Realizar un filtrado básico a los datos. Ejemplo solo seleccionar cierto grupo de categorias
# Procesamiento en Mongo Db
# Exportar los datos a mongo DB
# Crear 2 graficos con los datos
# Compartir link donde encontrar los datos

import requests

# URL del archivo ZIP
url = 'https://netsg.cs.sfu.ca/youtubedata/0333.zip'

# Nombre del archivo a guardar
zip_file = '0333.zip'

# Descargar el archivo ZIP
response = requests.get(url)
with open(zip_file, 'wb') as file:
    file.write(response.content)

print("Descarga completada.")

#Se importa archivos ZIP:
import zipfile
import os

# Ruta para descomprimir el archivo
extract_folder = 'youtube_data'

# Crear la carpeta de destino
os.makedirs(extract_folder, exist_ok=True)

# Descomprimir el archivo ZIP
with zipfile.ZipFile(zip_file, 'r') as zip_ref:
    zip_ref.extractall(extract_folder)

print("Descompresión completada.")

#Se importa la librería pandas
import pandas as pd

# Listar archivos descomprimidos
files = os.listdir(extract_folder)
print("Archivos descomprimidos:", files)

# Leer el primer archivo CSV
csv_file = os.path.join(extract_folder, files[0])
df = pd.read_csv(csv_file, sep='\t', header=None)

# Mostrar las primeras filas del dataframe
print(df.head())