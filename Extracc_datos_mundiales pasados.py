from bs4 import BeautifulSoup
import requests
import pandas as pd

years = [1991, 1995, 1999, 2003, 2007, 2011, 2015, 2019]

#Creamos una función, una vez que hayamos completado, METEMOS TOD0 A LA FUNCIÓN, para así obtener así automatizar los años restantes

def get_matches(year):
    web = f"https://es.wikipedia.org/wiki/Copa_Mundial_Femenina_de_F%C3%BAtbol_de_{year}"    #El enlace lleva un patrón, por ende convierto en cadena f" {}
    response = requests.get(web)
    content = response.text
    soup = BeautifulSoup(content, 'lxml')

    if year == 2023:
        matches = soup.find_all("table", class_="vevent plainlist")   #luego de hacer el match de abajo, creamos df
    else:
        matches = soup.find_all("table", class_="collapsible autocollapse vevent plainlist")

    Local = []
    Marcador = []
    Visita =[]

    for match in matches:
        Local.append(match.find('td',align="right").find("a").get_text()) #al finalizar con .get_text, obtenemos el texto de la clase; // print(match.find('td',align="right").find("a").get_text()) //
        Marcador.append(match.find('td',align="center").find("div").get_text())
        Visita.append(match.find('td',align="left").get_text())            #sin el .find(a), creo que solo se puede ejecutar una vez

    dict_futbol = {"Local": Local , "Marcador": Marcador, "Visita": Visita}
    df_futbol = pd.DataFrame(dict_futbol)
    df_futbol["Visita"] = df_futbol["Visita"].str.strip()      #Al parecer Visita vino con \n al final de cada país, se suprime con ambos codigos -> = df_futbol["Visita"].replace('\n', '', regex=True) 
    df_futbol["year"] = year
    return df_futbol
# get_matches(2019)

#Para Data Histórica
fifa = [get_matches(year) for year in years]         #list compression  #Se hace un bucle for para traer el mundial de todos los años -> for year in years:\n get_matches(year)
df_fifa = pd.concat(fifa, ignore_index=True)         #Concatena todos los DF, DF1, DF2, DF3...
# print(df_fifa)
df_fifa.to_csv("fifa_worldcup_historial_data.csv", index=False)

#Para fixture
df_fixture = get_matches(2023) 
df_fixture.to_csv("fifa_worldcup_fixture.csv", index=False)



"https://es.wikipedia.org/wiki/Copa_Mundial_Femenina_de_F%C3%BAtbol_de_2019"
"https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_sql.html#compare-with-sql"