


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

df = pd.read_csv(r"C:\Users\User\OneDrive\Documentos\Universidad\Auto 1\spotify-2023.csv", encoding='latin1')
print(df.head())

#Punto A: Cargue los datos e identifique cuantas variables categóricas (tipo object) y cuantas variables numéricas tiene.
print('\nPunto A:\n')
print(df.info()) 
print('\n')
print(df.dtypes.value_counts())

#Tiene 7 variables tipo object y 17 tipo int64

print('\n')

#Punto B: Desarrolle un algoritmo que nos diga cuantas canciones de Coldplay hay en la base de datos.
print('Punto B:\n')
algorit= df[df['artist(s)_name']=='Coldplay'].sum()
print(algorit)

print('\nColdplay tiene', algorit['artist_count'], 'canciones en la base de datos')
print('\n')

#Punto C: Encuentre el máximo y el mínimo de cada columna numérica en la base de datos.
print('\nPunto C:\n')
colnumericas=df.select_dtypes(include=['number'])

maximos=colnumericas.max()
minimos=colnumericas.min()

print("Máximos por columna:\n", maximos)
print("\nMínimos por columna:\n", minimos)

#Punto D:  Desarrolle una función que reciba como parámetro su base de datos y un artista y le devuelva todas las canciones de ese artista en base de datos.

print('\nPunto D:\n')

def artist_nom(df):
    nameartist = input("Ingrese el nombre del artista: ")
    artista = df[df['artist(s)_name'] == nameartist]

    if not artista.empty:   
        print(f"\nLas canciones de {nameartist} son:\n")
        print(artista['track_name'].to_string(index=False))
    else:
        print("\nEl artista no está en la base de datos")

artist_nom(df)

#Punto E: Cree una tabla con una función de agregación, que muestre la sumatoria de cuantas canciones Taylor Swift y Coldplay aparecen en playlist.

print('\nPunto E:\n')

def canciones_taylor_coldplay(df):

    filtro = df[df['artist(s)_name'].isin(['Taylor Swift', 'Coldplay'])]
   
    tabla = filtro.groupby('artist(s)_name').agg({'track_name':'count'})

    tabla = tabla.rename(columns={'track_name':'Cantidad de canciones'})
    
    return tabla

print(canciones_taylor_coldplay(df))


#Punto F: Desarrolle un subplot con dos gráficos, el primero es un boxplot relacione artist_count (eje x) con streams, y el segundo un histograma de los años de lanzamiento.

fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(12,5))

df.boxplot(column='streams', by='artist_count', ax=axs[0])
axs[0].set_title("Box Plot - Streams por Artist_Count")
axs[0].set_xlabel("Artist_Count")
axs[0].set_ylabel("Streams")

axs[1].hist(df['released_year'], bins=20, color='purple', edgecolor='black')
axs[1].set_title("Histogram - Año de Lanzamiento")
axs[1].set_xlabel("Año")
axs[1].set_ylabel("Cantidad")

plt.suptitle("") 
plt.show()