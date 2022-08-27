# Objtivo: importar la clasificación de la tabla de la Liga de futbol del diario AS

# instalamos pandas, requests, beautifulsoup4
# Ej: utilizamos pip install pandas

#Primero importamos las librerias necesarias

from cgitb import html
from typing import List
from bs4 import BeautifulSoup
import requests
import pandas as pd

# primero nos descargamos el HTML utilizando requests

url = 'https://resultados.as.com/resultados/futbol/primera/clasificacion/'
page = requests.get(url)

# ahora lo pasamos a formato BeautifulSoup quer nos permitirá identificar distintos elementos del HTML (se utiliza el html.parser para que lo interprete como HTML)

soup= BeautifulSoup(page.content, 'html.parser')

# ahora con el inspeccionador de codigo del navegador vemos como se presenta la informacion en el HTML
# Logramos ver que el nombvre del equipo se encuentra dentro de una etiqueta de tipo span y con una clase "nombre-equipo"

#identificamos los equipo
    # se escribe class seguido de una _ para que lo identifique como clase
eq = soup.find_all('span', class_="nombre-equipo" )

# metemos los datos encontrados dentro de una lista llamada equipos

equipos = list()

# para agregar los elementos iteramos sobre eq


count = 0; # debido a que nos devuelve os nombres de los equipos repetidos, limitamos la lista a los primeros 20
for i in eq:
    if count<20:
    # como solo nos interesa el texto( nombre del equipo):
        equipos.append(i.text)
    else:
        break
    count +=1

# ahora hacemnos los mismo pero con los puntos (etiqueta td y clase "Destacado")

pt = soup.find_all('td', class_="destacado" )

# metemos los datos encontrados dentro de una lista llamada puntos

puntos = list()

# para agregar los elementos iteramos sobre pt

count = 0; # debido a que nos devuelve os nombres de los equipos repetidos, limitamos la lista a los primeros 20
for i in pt:
    if count<20:
    # como solo nos interesa el texto( nombre del equipo):
        puntos.append(i.text)
    else:
        break
    count +=1

# ahora con ambos datos de puntos y equipos los introducimos en un dataframe (para esto importamos pandas)

df = pd.DataFrame({'Nombre': equipos, 'Puntos': puntos}, index=list(range(1,21)))

# podemos guardar este dataframe como un csv por ejemplo:
# Agregamos Index a False para que no lo guarde
df.to_csv('Clasificación liga Santander.csv', index=False)
