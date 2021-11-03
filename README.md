# ziicube_scraping
Script que et descarrega un arxiu csv amb la llista dels 20 productes més venuts de la web de cubs de Rubik https://www.ziicube.com
# Configuració
Per poder executar el codi, cal instal·lar una serie de paquets. La forma més senzilla és crear un nou entorn amb Anaconda i el fitxer [ziicube_scraping.yml](ziicube_scraping.yml). Només cal executar la següent ordre a la consola:
```
conda env create -f ziicube_scraping.yml
```
També hi ha la opció d'instal·lar manualment cada un dels paquets:
```
pip install tqdm
pip install builtwith
pip install requests
pip install pandas
pip install beautifulsoup4
pip install lxml
```
# Execució
Per iniciar el procés, cal executar el fitxer [ziicube_scraping.py](ziicube_scraping.py) a la consola mitjançant el següent ordre:
```
python ziicube_scraping.py
```
# Resultats
Un  cop executat l'script, els resultats es guardaran al fitxer [ziicube_30day_bestseller.csv](ziicube_30day_bestseller.csv).
En aquest arxiu hi ha la relació dels 20 productes més venuts amb els següents atributs:
- ***pos***: Posició en el ràrquing dels més venuts	
- ***id***:	Codi d'identificació del producte
- ***name***: Nom del producte
- ***price***: Preu del producte en $
- ***rat***: Valoració del producte per part dels consumidors (0-100)
- ***likes***: Número de m'agrades que ha rebut el producte
- ***brand_name***:	Nom de l'empresa que produeix el producte
- ***web***: Pàgina web del producte


[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5644225.svg)](https://doi.org/10.5281/zenodo.5644225)

# Documentació


# Llicència
<a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/"><img alt="Llicència de Creative Commons" style="border-width:0" src="https://i.creativecommons.org/l/by-nc/4.0/88x31.png" /></a><br />Aquesta obra està subjecta a una llicència de <a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/">Reconeixement-NoComercial 4.0 Internacional de Creative Commons</a>
