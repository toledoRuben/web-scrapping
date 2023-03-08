import urllib.request as request
import os
import re
import urllib.request as request
from bs4 import BeautifulSoup



#**Encabezados**#
#comprobar todos los encabezados
site = request.urlopen("http://python.org")
soup = BeautifulSoup(site)
for h1 in soup.find_all("h1"):
    print("esto es un encabezado h1 : ", h1)
print("En total son :", len(soup.find_all("h1")))

#**Enlaces rotos**#
#//añadir los enlaces de la pagina a una lista
site = request.urlopen("http://python.org")
soup = BeautifulSoup(site)
enlaces = []
elementos = soup.select("a")
for enlace in elementos:
    link = enlace.get("href")
    if (link.startswith("http")):
        enlaces.append(link)
print(enlaces)
#//comprobar si los 10 primeros enlaces estan rotos
for ennlac in enlaces[:10]:
    petition = request.urlopen(ennlac)
    print("Enlace:", ennlac, "Respuesta :", petition.code)

#**Comprobar si tiene icono**#

site = request.urlopen("http://python.org")
soup = BeautifulSoup(site)
icon_link = soup.find("link", rel="icon")
icon = request.urlopen("http://python.org"+icon_link["href"])
with open("test.ico", 'wb') as  f:
    try:
        f.write(icon.read())
        print("escrito")
    except :
        print("no hay icono")

#**Comprobar si tiene google analytics**#
site = request.urlopen("http://python.org")
soup = BeautifulSoup(site)
if(soup.find_all(text=re.compile(".google-analytics"))):
    print("contiene google analytics")
else:
    print("no tiene google analytics")

#**idioma**#

site = request.urlopen("http://python.org")
soup = BeautifulSoup(site,"html.parser")
lang = soup.find("html")["lang"]
print("El idioma del sitio web es :",lang)

#**Charset**#
site = request.urlopen("http://python.org")
print("pagina :", site)
meta = site.info()
print("Content type :", site.headers["Content-Type"])

#**ViewPort**#

site = request.urlopen("http://python.org")
soup = BeautifulSoup(site)
print("ViewPort :",soup.find("meta", attrs={"name" : "viewport"}))

