import sqlite3
conn = sqlite3.connect('kontakty.db')
conn.executescript("""DROP TABLE IF EXISTS kontakty;
            CREATE TABLE IF NOT EXISTS kontakty(
            NUMBER INT PRIMARY KEY NOT NULL,
            NAME TEXT NOT NULL,
            SURNAME TEXT NOT NULL);""")
conn.execute("INSERT INTO kontakty (NUMBER,NAME,SURNAME) VALUES ('665474747', 'marek', 'drozdzik')")
conn.execute("INSERT INTO kontakty (NUMBER,NAME,SURNAME) VALUES ('605474747', 'pablo', 'escobar')")
conn.execute("INSERT INTO kontakty (NUMBER,NAME,SURNAME) VALUES ('669474747', 'gabi', 'zabi')")
cursor = conn.execute("SELECT NUMBER, NAME, SURNAME from kontakty")
def AddNumber():
    number = int(input("Podaj numer telefonu: "))
    name = input("Podaj imie: ")
    surname = input("Podaj nazwisko: ")
    conn.execute("INSERT INTO kontakty (NUMBER,NAME,SURNAME) VALUES ('{}', '{}', '{}')".format(number, name, surname))
def ShowAllNumbers():
    rows = cursor.fetchall()
    for row in rows:
        print(row)
def Search(options, value):
    if options == 1:
        with conn:
            print(cursor.execute(f'SELECT * FROM kontakty WHERE NUMBER = "{value}";'))
    elif options == 2:
        with conn:
            print(cursor.execute(f'SELECT * FROM kontakty WHERE NAME = "{value}";'))
    elif options == 3:
        with conn:
            cur = conn.execute(f'SELECT * FROM kontakty WHERE surname = "{value}";')
            for row in cur:
                print(row)
AddNumber()
ShowAllNumbers()