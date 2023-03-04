import sqlite3
import hashlib
import random
import datetime
import json
import os



date = str(datetime.datetime.now().date())


database_name= os.path.abspath("Tombola_Bingo/game.db")




### makes empty dictionary
dictionary = dict()
### Makes random numbers dictionary with winnings ###
def generate_numbers():
    numbers = list(range(1, 49))
    random.shuffle(numbers)
    arrayWinnings=[11000,12000,13000,14000,16000,10000,7500,5000,2500,1000,500,300,200,150,100,90,80,70,60,50,40,30,25,20,15,10,9,8,7,6,5,4,3,2,1]
    numbersRandom= numbers[:35]
    dictionary = dict(zip(arrayWinnings, numbersRandom))
    return dictionary


### RETURNS SHA1 hash of the string ###


def get_sha1(input_string):
    sha1 = hashlib.sha1()
    sha1.update(input_string.encode('utf-8'))
    return sha1.hexdigest()
    

new_id = 0

### Reads the database to create id and makes an array of numbers selected this round.
def add_id():
    
    conn = sqlite3.connect(database_name)
    c = conn.cursor()

    c.execute("SELECT id FROM numbers_played ORDER BY id DESC LIMIT 1")
    max_id = c.fetchone()[0]
    print(max_id)
    global new_id
    if max_id:
        
        new_id = max_id + 1
        new_id = get_sha1(str(new_id)+get_sha1("SECRET_KEY"))
    else:
        new_id = 1
        new_id= get_sha1(str(new_id)+get_sha1("SECRET_KEY"))
    return new_id
            
### Returns an array 
class testClass():
    def __init__(self,id,databaseName):
        self.conn = sqlite3.connect(database_name)
        self.cursor = self.conn.cursor()
        self.numbers=generate_numbers()
        self.serial = add_id()
        
        def insert_row(database_name, serial, numbers):
            self.c = self.conn.cursor()

            # Convert the dictionary to a JSON string
            dict_as_json = json.dumps(self.numbers)
            print(dict_as_json)
            self.c.execute("INSERT INTO numbers_played (serial, numbers, date) VALUES (?, ?, ?)", (serial, dict_as_json, date))
            self.conn.commit()
            self.conn.close()


       
        insert_row(self,new_id,dictionary)


test= testClass(1,database_name)




