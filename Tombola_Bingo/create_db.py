import sqlite3
import random
import os

database_name= os.path.abspath("Tombola_Bingo/game.db")

def create_table(database_name):
    conn = sqlite3.connect(database_name)
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS numbers_played (id INTEGER PRIMARY KEY,serial TEXT, numbers TEXT, date TEXT)")
    conn.commit()
    conn.close()



def insert_empty_row():
    conn = sqlite3.connect(database_name)
    c = conn.cursor()
    c.execute("INSERT INTO numbers_played (serial,numbers, date) VALUES (NULL, NULL, NULL)")
    conn.commit()
    conn.close()




def create_database():
    conn = sqlite3.connect(database_name)
    c = conn.cursor()
    c.execute("""CREATE TABLE numbers_played (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    serial INTEGER,
                    numbers TEXT,
                    date TEXT
                )""")
    conn.commit()
    conn.close()

def create_tickets_table():
    conn = sqlite3.connect(database_name)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS tickets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            numbers TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

class Ticket:
    def __init__(self, numbers=None):
        self.numbers = numbers or random.sample(range(1, 50), 6)


    def insert_into_database(self):
            conn = sqlite3.connect(database_name)
            c = conn.cursor()
            c.execute("""
                INSERT INTO tickets (numbers)
                VALUES (?)
            """, (str(sorted(self.numbers)),))
            ticket_id = c.lastrowid
            conn.commit()
            conn.close()
            return ticket_id
    
ticket1=Ticket((1,2,3,4,5,6))
print(ticket1)


def read_all_tickets():
    conn = sqlite3.connect(database_name)
    c = conn.cursor()
    c.execute("SELECT * FROM tickets")
    tickets = c.fetchall()
    conn.close()
    return tickets




def create_tickets_table():
    conn = sqlite3.connect(database_name)
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS tickets (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    serialId TEXT NOT NULL,
                    gameId TEXT NOT NULL,
                    numbers TEXT NOT NULL,
                    money INTEGER NOT NULL,
                    money_won INTEGER,
                    is_winner BOOLEAN NOT NULL)""")
    conn.commit()
    conn.close()

def drop_all_tickets():
    conn= sqlite3.connect(database_name)
    c = conn.cursor()
    c.execute("DROP TABLE tickets")
    conn.close()
    return "Succeeded"


def read_all_tickets():
    conn = sqlite3.connect(database_name)
    c = conn.cursor()
    c.execute("SELECT * FROM tickets")
    tickets = c.fetchall()
    conn.close()
    return tickets


def insert_empty_ticket():
    conn = sqlite3.connect(database_name)
    c = conn.cursor()
    c.execute("INSERT INTO tickets (serial_Id, game_Id, numbers, money) VALUES (?,?,?,?)", (None, None, None, None))
    conn.commit()
    conn.close()



def add_is_winner_column():
    conn = sqlite3.connect("game.db")
    c = conn.cursor()
    c.execute("ALTER TABLE tickets ADD COLUMN is_winner BOOLEAN DEFAULT NULL")
    conn.commit()
    conn.close()

create_tickets_table()