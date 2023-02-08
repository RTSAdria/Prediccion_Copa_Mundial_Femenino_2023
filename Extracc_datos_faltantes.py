from bs4 import BeautifulSoup
import requests
import pandas as pd


def get_matches(year):
    web = "https://es.wikipedia.org/wiki/Copa_Mundial_Femenina_de_F%C3%BAtbol_de_2023"    #El enlace lleva un patrón, por ende convierto en cadena f" {}
    response = requests.get(web)
    content = response.text
    soup = BeautifulSoup(content, 'lxml')

    year == 2023
    matches = soup.find_all("table", class_="vevent plainlist")  
    Local = []
    Marcador = []
    Visita =[]

    for match in matches:
        Local.append(match.find('td',align="right").get_text()) 
        Marcador.append(match.find('td',align="center").find("div").get_text())
        Visita.append(match.find('td',align="left").get_text())         

    dict_futbol = {"Local": Local , "Marcador": Marcador, "Visita": Visita}
    df_futbol = pd.DataFrame(dict_futbol)
    df_futbol["Local"] = df_futbol["Local"].str.strip()
    df_futbol["Visita"] = df_futbol["Visita"].str.strip()      
    df_futbol["year"] = 2023
    return df_futbol

df_fixture = get_matches(2023) 
df_fixture.to_csv("fifa_worldcup_fixture_faltante.csv", index=False)