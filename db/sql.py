import sqlite3, json

class DataBases:
    def create_tables(self):
        connection=sqlite3.connect("db/naturesDb")
        cursor=connection.cursor()
        cursor.execute("CREATE TABLE NATURES (NAMES VARCHAR(7), ATTACK DECIMAL, DEFENSE DECIMAL, SPATTACK DECIMAL, SPDEFENSE DECIMAL, SPEED DECIMAL)")
        #cursor.execute("CREATE TABLE MOVES_NAMES(NAMES VARCHAR(30))")
        connection.commit()
        connection.close()
        
    def natures(self):
        connection=sqlite3.connect("db/globalDb")
        cursor=connection.cursor()

        cursor.execute("""INSERT INTO NATURES VALUES
        ('Lonely',0.1,-0.1,0,0,0),
        ('Brave',0.1,0,0,0,-0.1),
        ('Adamant',0.1,0,-0.1,0,0),
        ('Naughty',0.1,0,0,-0.1,0),

        ('Bold',-0.1,0.1,0,0,0),
        ('Relaxed',0,0.1,0,0,-0.1),
        ('Impish',0,0.1,-0.1,0,0),
        ('Lax',0,0.1,0,-0.1,0),

        ('Modest',-0.1,0,0.1,0,0),
        ('Mild',0,-0.1,0.1,0,0),
        ('Quiet',0,0,0.1,0,-0.1),
        ('Rash',0,0,0.1,-0.1,0),

        ('Calm',-0.1,0,0,0.1,0),
        ('Gentle',0,-0.1,0,0.1,0),
        ('Sassy',0,0,0,0.1,-0.1),
        ('Careful',0,0,-0.1,0.1,0),

        ('Timid',-0.1,0,0,0,0.1),
        ('Hasty',0,-0.1,0,0,0.1),
        ('Jolly',0,0,-0.1,0,0.1),
        ('Naive',0,0,0,-0.1,0.1),
       
        ('Hardy',0,0,0,0,0),
        ('Docile',0,0,0,0,0),
        ('Serious',0,0,0,0,0),
        ('Bashful',0,0,0,0,0),
        ('Quirky',0,0,0,0,0)
        """)
        connection.commit()
        connection.close
    
    #Putting info from a list in a table
    """
    def pokemonNames(self):
        with open("db/movesNames.json","r") as file:
            moves_db=json.load(file)
            names_array=[]
            for i in moves_db:
                names_array.append(i)
            file.close()
            return names_array
    
    def tableNames(self,names_array):
        connection=sqlite3.connect("db/globalDb")
        cursor=connection.cursor()

        for i in names_array:
            cursor.execute("INSERT INTO MOVES_NAMES VALUES(?)",(i,))

        connection.commit()
        connection.close()
    """
    #Example: checking if a file exists
    """
    def open(self):
        try:
            open ("ab.txt")
        except FileNotFoundError:
            pass
    """

dataClass=DataBases()
try:
    dataClass.create_tables()
except Exception:
    pass
dataClass.natures()
