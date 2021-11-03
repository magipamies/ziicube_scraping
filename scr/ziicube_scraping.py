"""
Script que extreu la llista dels 20 productes mes venuts de la web www.ziixube.com.
Guarda la llista en un arxiu csv.
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
from tqdm import tqdm

# Pàgina d'on obtenir la informació
str = 'https://www.ziicube.com/'

# Columnes de la base de dades
columns_df = ['pos', 'id', 'name', 'price', 'rat', 'likes', 'brand_name', 'web']


# ---------------------------------------------
def cubs_attr(web):
    attr_dict = {}
    # str_2 = 'https://www.ziicube.com/YJ-333-GuanLong-Plus-V3'
    page_f = requests.get(web)
    soup_f = BeautifulSoup(page_f.content, features="lxml")

    attr = soup_f.find('div', {"class": "sku-attr"})
    attr_dict['brand_name'] = attr.find('td', {"class": 'dd'}).a.string

    rat = soup_f.find('div', {"class": "sku-rating"})

    attr_dict['rat'] = int(re.findall(r'\d+', rat.b['style'])[0])

    attr_dict['likes'] = rat.find('i', {"class": "coO"}).string

    return attr_dict

# -------------------------------------------------

# Descarreguem la pagina web
page = requests.get(str)

# Creem un objecte BeautifulSoup a partir de la pagina
soup = BeautifulSoup(page.content, features="lxml")

# Guardem la part de la pàgina que conté la informació que ens interessa
uu = soup.find('ul', {"class": "content"})

# Creem un diccionari per guardar-hi la informaci de cada cub
dic_cubs = {}

# Intinerem per a cada cub per treure-li la informació
print('Iniciant el proces de web scraping')
for cub in tqdm(uu.find_all('li')):
    # Creem un diccionari per guardar la informacio del cub
    dic_cub = {}

    # Cerquem la informacio de cada variable
    dic_cub['id'] = cub.find('div', {"class": "detail"})['data-id']
    dic_cub['web'] = cub.find('div', {"class": "detail"}).a['href']
    dic_cub['name'] = cub.find('div', {"class": "detail"}).a.string
    dic_cub['pos'] = cub.find('div', {"class": "num"}).string
    dic_cub['price'] = format(float(cub.find('div', {"class": "price"}).string.strip("$")),".2f")

    # Utilitzem la funcio "cubs_attr" per obtenir la informacio ubicada a la web del cub.
    dic_cub.update(cubs_attr(dic_cub['web']))

    # Guardem el diccionari al diccionari "dic_cubs".
    dic_cubs[dic_cub['id']] = dic_cub

# Creem un dataframe de pandas a partir del diccionari que guarda la informacio de tots els cubs.
cubs_db = pd.DataFrame.from_dict(dic_cubs, orient='index', columns = columns_df)

# Guardem el dataframe en un arxiu csv
cubs_db.to_csv("ziicube_30day_bestseller.csv", index=False)


print('Procés finalitzat')
