#save_and_get_back_pkm_sets
from assets.pokemon_models import *
import sqlite3

class Save:
    """def __init__(self,pokemon1:Pokemon,pokemon2:Pokemon):
        self.pokemon1=pokemon1
        self.pokemon2=pokemon2
    """
    def create_tables(self):
        connector=sqlite3.connect("db/pokemonSetsDb")
        cursor=connector.cursor()
        
        #create all tables
        cursor.execute("""CREATE TABLE IF NOT EXISTS POKEMON_SETS 
        (PKM_NAME VARCHAR(15),
        TYPE_1 VARCHAR(9),
        TYPE_2 VARCHAR(9),
        NATURE VARCHAR(7),
        LEVEL INTEGER)""")

        cursor.execute("""CREATE TABLE IF NOT EXISTS MOVES 
        (PKM_NAME VARCHAR(15),
        MOVE_NAME VARCHAR(20),
        TYPE VARCHAR(9),
        CATEGORY VARCHAR(8),
        POWER INTEGER,
        ACCURACITY INTEGER,
        PP INTEGER)""")

        cursor.execute("""CREATE TABLE IF NOT EXISTS BASE_STATS 
            (NAME VARCHAR(15),
            BASE_HP INTEGER, 
            BASE_ATTACK INTEGER, 
            BASE_DEFENSE INTEGER, 
            BASE_SPATTACK INTEGER, 
            BASE_SPDEFENSE INTEGER, 
            BASE_SPEED INTEGER)""")
            
        cursor.execute("""CREATE TABLE IF NOT EXISTS IVS
            (PKM_NAME VARCHAR(15),
            HP_IVS INTEGER, 
            ATTACK_IVS INTEGER, 
            DEFENSE_IVS INTEGER, 
            SPATTACK_IVS INTEGER, 
            SPDEFENSE_IVS INTEGER, 
            SPEED_IVS INTEGER)""")

        cursor.execute("""CREATE TABLE IF NOT EXISTS EVS
            (PKM_NAME VARCHAR(15),
            HP_EVS INTEGER, 
            ATTACK_EVS INTEGER, 
            DEFENSE_EVS INTEGER, 
            SPATTACK_EVS INTEGER, 
            SPDEFENSE_EVS INTEGER, 
            SPEED_EVS INTEGER)""")

        cursor.execute("""CREATE TABLE IF NOT EXISTS ACTUAL_STATS 
            (PKM_NAME VARCHAR(15),
            ACTUAL_HP INTEGER, 
            ACTUAL_ATTACK INTEGER, 
            ACTUAL_DEFENSE INTEGER, 
            ACTUAL_SPATTACK INTEGER, 
            ACTUAL_SPDEFENSE INTEGER, 
            ACTUAL_SPEED INTEGER)""")
            
        connector.commit()
        connector.close()