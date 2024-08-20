# Lea el archivo 'winemag-data-130k-v2.csv' y realice lo siguiente:
#Explore el dataframe según lo visto en clase
#Realice al menos 4 renombre de columna y 3 creación de nuevas columnas según criterio. Deberá crear las columnas 
# que crea conveniente. Ejemplo: Según el país etiquetelos según continente.
#Genere 4 reportes distintos(podria agrupando, filtrar, ordenar, etc). Deberá elegir que reportes realizar

#Ejemplo: Por contienente mostrar los vinos mejor puntuados
#Ejemplo2: Promedio de precio de vino y cantidad de reviews obtenidos según pais. Ordenado de mejor a peor.
#Exporte los 4 reportes a 4 formatos de archivos diversos, csv, excel, sqllite, mongodb...
#Para guardar datos de datos agrupados, puede revisar esta solución
#  https://stackoverflow.com/questions/25789264/pandas-dataframegroupby-export-to-excel

#Solución:

import pandas as pd
# Leer el archivo CSV
df = pd.read_csv('winemag-data-130k-v2.csv')
# Verificar las primeras filas del DataFrame
print(df.head())

# Verificar las dimensiones del DataFrame, filas y columnas:
print(df.shape)

# Verificar los nombres de las columnas
print(df.columns)

# Resumen de información del DataFrame
print(df.info())

# Estadísticas descriptivas de las columnas numéricas
print(df.describe())

# Renombrar columnas
df.rename(columns={
    'country': 'Country',
    'points': 'Rating',
    'price': 'Price',
    'variety': 'Variety'
}, inplace=True)

# Verificar el cambio
print(df.columns)

# Se crea la columna precio por categoría 'Price_Category'
df['Price_Category'] = pd.cut(df['Price'], bins=[0, 20, 50, 100, float('inf')], labels=['Cheap', 'Affordable', 
'Expensive', 'Luxury'])

# Crear la columna 'Continent'
continent_map = {
    'US': 'North America', 'France': 'Europe', 'Italy': 'Europe', 'Spain': 'Europe', 
    'Portugal': 'Europe', 'Chile': 'South America', 'Argentina': 'South America', 
    'Australia': 'Oceania', 'New Zealand': 'Oceania', 'South Africa': 'Africa'
}
df['Continent'] = df['Country'].map(continent_map)

# Crear la columna 'Value_for_Money'
df['Value_for_Money'] = df['Rating'] / df['Price']

# Verificar las nuevas columnas
print(df.head())

winemag-data-130k-v2.csv

https://github.com/gdelgador/ProgramacionPython202401/blob/main/Modulo5/src/winemag-data-130k-v2.csv
País según continente:

https://gist.githubusercontent.com/kintero/7d1db891401f56256c79/raw/a61f6d0dda82c3f04d2e6e76c3870552ef6cf0c6/paises.csv