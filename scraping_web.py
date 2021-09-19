from os import name
from assets.constants import *
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

def get_moves_info():
    #request and parse with bs4
    url="https://pokemondb.net/move/all" 
    page_response=requests.get(url,timeout=5)
    page_content=bs4.BeautifulSoup(page_response.content, features="html.parser")

    #Find all table items
    page_rows=page_content.find_all("tr")
   
    moves_data={}
    for row in page_rows[2:]:
        #move name
        move_name=row.find("a", attrs={"class":"ent-name"}).text 
        if move_name in moves_data:
            break
        #move type
        move_type=row.find("a", attrs={"class":"type-icon"}).text
        
        #move category
        move_category=row.find("img", attrs={"class":"img-fixed"})
        if str(move_category)=="""<img alt="Physical" class="img-fixed" height="20" loading="lazy" src="https://img.pokemondb.net/images/icons/move-physical.png" title="Physical" width="30"/>""":
            move_category="Physical"
        elif str(move_category)=="""<img alt="Special" class="img-fixed" height="20" loading="lazy" src="https://img.pokemondb.net/images/icons/move-special.png" title="Special" width="30"/>""":
            move_category="Special"
        elif str(move_category)=="""<img alt="Status" class="img-fixed" height="20" loading="lazy" src="https://img.pokemondb.net/images/icons/move-status.png" title="Status" width="30"/>""":
            move_category="Status"
        elif str(move_category)=="None":
            move_category="Both"

        #power/accuracity/pp
        if move_category=="Status":
            pass
        else:
            move_stats=row.find_all("td")[3:6]
            move_stats=list(map(lambda data: data.text,move_stats))
        
        #text probability like freeze,etc
        effect_probability=row.find("td",attrs={"class":"cell-long-text"}).find_next("td",attrs={"class":"cell-num"}).text
       
        #text
        move_effect=row.find("td",attrs={"class":"cell-long-text"}).text
        
        #save info in a dictitionary
        if move_category!="Both":
            moves_data[move_name]={
                "Type":move_type,
                "Category":move_category
            }
       
        else:
            moves_data[move_name]={
                "Type":move_type,    
                }  
    
        if move_category!="Status":
            moves_data[move_name]["Power"]=move_stats[0]
            moves_data[move_name]["Accuracity"]=move_stats[1]
        moves_data[move_name]["Pp"]=move_stats[2]
        moves_data[move_name]["Effect"]=move_effect
         
        if effect_probability=='—':pass
        else:
            moves_data[move_name]["EffectProbability"]=int(effect_probability)
        
        #Save info in json file
        with open("db/moves.json","w") as file:
           json.dump(moves_data,file)

get_moves_info()
       

