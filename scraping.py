# importacion de librerias

from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://resultados.as.com/resultados/futbol/tercera/clasificacion/?omnil=src-sab'
# descarga la informacion de la pagina
page = requests.get(url)

# usaremos libreria Bearetifulsoup que poder identificar mas claramente elementos html

soup = BeautifulSoup(page.content, 'html.parser')

# Obteniendo equipos

# se debe usar class_ para que python lo interprete como una clase externa en este caso html
equip = soup.find_all('cite', class_ = 'iUh30 bc tjvcx')

lista_equip = list()

#iteramos el equip para sacar los nombre solamente
# para ver los 20 primeros iniciamos un contador

count = 0
for i in equip:
    if count < 20:
        lista_equip.append(i.text)
        count+=1

#descargamos ahora la puntuacion de cada equipo
pts = soup.find_all('td', class_ = 'destacado')

lista_pts = list()
count = 0
for i in pts:
    if count < 20:
        lista_pts.append(i.text)
        count+=1
        
print (lista_equip)
print (lista_pts)

#Ahora con Panda  vamos a meter los datos en un dataframe 

df = pd.DataFrame({'Nombre': lista_equip , 'Puntos': lista_pts }, index=list(range(1,21)))

# podemos pasarlo a un archivo csv

df.to_csv('Clasificacion.csv', index=False)