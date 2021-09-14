from assets.constants import *
from typing import Text
import bs4 
import requests
import json



def get_pokemon_info():
   
    #request and parse with bs4
    url="https://pokemondb.net/pokedex/all" 
    page_response=requests.get(url,timeout=5)
    page_content=bs4.BeautifulSoup(page_response.content, features="html.parser")
    
    #Find all table items
    page_rows=page_content.find_all("tr")
    
    pokemon_data={}
    for row in page_rows[1:]:
        #Pokemon Name
        pokemon_name=row.find("a", attrs={"class":"ent-name"}).text 
        pokemon_extra_name=row.find("small", attrs={"class":"text-muted"})
        if pokemon_extra_name:
            pokemon_name=pokemon_extra_name.text
        
        #Pokemon Types
        pokemon_type1=row.find("a", attrs={"class":"type-icon"}).text
        pokemon_type2=row.find("a", attrs={"class":"type-icon"}).find_next("a", attrs={"class":"type-icon"}).text
       
        #Pokemon Stats
        stats_html=row.find_all("td")[4:]
        stats_array=list(map(lambda data: int(data.text),stats_html))
    
        #Save info in dictionary
        if pokemon_type1==pokemon_type2:
            pokemon_data[pokemon_name]={
                "Type1":pokemon_type1,
                "Stats":{
                    HP: stats_array[0],
                    ATTACK: stats_array[1],
                    DEFENSE: stats_array[2],
                    SPATTACK: stats_array[3],
                    SPDEFENSE: stats_array[4],  
                    SPEED: stats_array[5],
                }    
            }
        else:
            pokemon_data[pokemon_name]={
                "Type1":pokemon_type1,
                "Type2":pokemon_type2,
                "Stats":{
                    HP: stats_array[0],
                    ATTACK: stats_array[1],
                    DEFENSE: stats_array[2],
                    SPATTACK: stats_array[3],
                    SPDEFENSE: stats_array[4],  
                    SPEED: stats_array[5],
                }    
        }
        #Save info in json file
        with open("db/pokemon.json","w") as file:
            json.dump(pokemon_data,file)
    



    

       

    
    