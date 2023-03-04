import sqlite3
import os
import json
import time

database_name= os.path.abspath("Tombola_Bingo/game.db")
dictionary={}

def make_number_from_string(input_string):
    result = ""
    for char in input_string:
        if char.isdigit():
            result += char
    return int(result) if result else None








def provera_Tiketa(brojTiketa):
    conn = sqlite3.connect(database_name)
    c=  conn.cursor()
    c.execute("SELECT gameId FROM tickets  WHERE id='{}'".format(brojTiketa))
    gameId= c.fetchall()
    gameId= gameId[0][0]
  
    c.execute("SELECT is_winner FROM tickets WHERE id='{}'".format(gameId))
    ticket_winnings = c.fetchall()
    c.execute("SELECT numbers FROM tickets WHERE id='{}'".format(brojTiketa))
    numbers_list = c.fetchall()
    c.execute("SELECT money FROM tickets WHERE id='{}'".format(brojTiketa))
    money = c.fetchall()
    numbers_array=[]
    numbersArray=[]
    for numbers in numbers_list:
        numbers_array = numbers[0].split(",") 
    numbers_array[0]=numbers_array[0][1]


    ###THIS FIXES MY BAD CODE IN JSON!!
    for i in range (0,6):
        numbersArray.append(numbers_array[i])
    numbers_array=[]
    number=0
    for i in numbersArray:
        number=make_number_from_string(i)
        numbers_array.append(number)
        

    c.execute("SELECT numbers FROM numbers_played WHERE id='{}'".format(gameId))
    dict_as_json = c.fetchone()[0]

    # Convert the JSON string back into a dictionary
    dictionary = json.loads(dict_as_json)

    
    winningArray=[]
    for key,value in dictionary.items():
        winningArray.append(value)
    


    count=0
    for i in winningArray:
        if i in numbers_array:
            count +=1
    print(count)

    multipliers=[]
    if count == 6 :
        
        for key,value in dictionary.items():
            if value in numbers_array:
                multipliers.append(int(key))
        print("ticket dobitan sa kvotom {}".format(min(multipliers)))
        
        money_won=int(min(multipliers))* money[0][0]
        print("Osvojili ste {} dinara".format(money_won))
        is_winner=True
        
    

    else: 
        print("nedobitan {} : broj tiketa".format(brojTiketa))
        is_winner = False   
    try:
        c.execute("UPDATE tickets SET money_won=? WHERE id=?", (money_won, brojTiketa))
    except: pass
    conn.commit()
    conn.close()

#provera_Tiketa(1591)
#provera_Tiketa(1592)


#for i in range(28690,28692):
 #  provera_Tiketa(i)


def isplata(gameId):
    conn = sqlite3.connect(database_name)
    c=  conn.cursor()
    c.execute("SELECT serialId FROM tickets WHERE gameId='{}'".format(gameId))
    ticket_winnings = c.fetchall()

    for i in range(0, len(ticket_winnings)):
        provera_Tiketa(ticket_winnings[i][0])

time_start=time.time()
provera_Tiketa(29406)
time_stop=time.time()
print(time_stop - time_start)