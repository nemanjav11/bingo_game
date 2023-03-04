import sqlite3
import os
import random

database_name= os.path.abspath("Tombola_Bingo/game.db")

class Ticket:
    
    def __init__(self, num1, num2, num3, num4, num5, num6, money):
        self.numbers=[]
        for i in num1,num2,num3,num4,num5,num6:
            if i > 49 or i<=0 or i in self.numbers:
                return print("ERROR: Ticket")
                
            else:
                self.numbers.append(i)
        self.numbers = [num1, num2, num3, num4, num5, num6]
        self.numbers.sort()
        print(self.numbers)
        self.lastId= self.get_last_id()
        self.money = money
        self.gameId=self.get_game_id()
        self.insert_ticket()
        self.printInfo()
                
        
    def get_last_id(self):
        conn = sqlite3.connect(database_name)
        c = conn.cursor()
        c.execute("SELECT MAX(id) FROM tickets")
        last_id = c.fetchone()[0]
        if last_id is None:
            self.lastId = 1
        else:
            self.lastId = last_id + 1
        conn.close()
        return self.lastId
        



    def get_game_id(self):
        conn = sqlite3.connect(database_name)
        c = conn.cursor()
        c.execute("SELECT MAX(id) FROM numbers_played")
        last_id = c.fetchone()[0]
        if last_id is None:
            self.gameId = 1
        else:
            self.gameId = last_id + 1
        conn.close()
        return self.gameId
     
    


    def insert_ticket(self):
        conn = sqlite3.connect(database_name)
        c = conn.cursor()
        c.execute("INSERT INTO tickets (serialId, gameId, numbers, money, is_winner) VALUES (?,?,?,?,FALSE)", (self.lastId, self.gameId, str(self.numbers),self.money))
        conn.commit()
        conn.close()

    def printInfo(self):
        print("Uplatili ste tiket sa brojevima : {} za iznos {}, za kolo broj {}, broj tiketa {} ! Srecno!".format(self.numbers,self.money,self.gameId, self.lastId))

a=Ticket(7,1,5,9,20,15,20)
money_players=[20,20,20,20,50,50,100,20]

for i in range(1,1000):
    Ticket(random.randrange(1,49),random.randrange(1,49),random.randrange(1,49),random.randrange(1,49),random.randrange(1,49),random.randrange(1,49),random.sample(money_players,1)[0])

