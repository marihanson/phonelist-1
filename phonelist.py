#import sqlite3
#conn = sqlite3.connect("phone.db")

import psycopg2
conn = psycopg2.connect(
            host="localhost",
            database="phone",
            user="phone",
            password="de2022"
        )

def read_phonelist(C):
    cur = C.cursor()
    cur.execute("SELECT * FROM phonelist;")
    rows = cur.fetchall()
    cur.close()
    return rows
def add_phone(C, name, phone, address):
    cur = C.cursor()
    cur.execute(f"INSERT INTO phonelist VALUES ('{name}', '{phone}', '{address}');")
    cur.close()
def delete_phone(C, name):
    cur = C.cursor()
    cur.execute(f"DELETE FROM phonelist WHERE name = '{name}';")
    cur.close()
def save_phonelist(C):
    cur = C.cursor()
    try:
        cur.execute("COMMIT;")
    except:
        print("No changes!")
    cur.close()
    
def print_help():
    print( '''Hello and welcome to the phone list. Available commands:
             HELP - View command options
             ADD - add a phone number
             DELETE - delete a contact
             LIST - list all phone numbers
             SAVE - save changes
             QUIT - quit the program''')

print_help()
while True: ## REPL - Read Execute Program Loop
    cmd = input("Command: ").upper()
    if cmd == "LIST":
        print(read_phonelist(conn))
    elif cmd == "ADD":
        name = input("  Name: ")
        phone = input("  Phone: ")
        address = input("  Address: ")
        add_phone(conn, name, phone, address)
    elif cmd == "DELETE":
        name = input("  Name: ")
        delete_phone(conn, name)
    elif cmd == "SAVE":
        save_phonelist(conn)
    elif cmd == "HELP":
        print_help()
    elif cmd == "QUIT":
        save_phonelist(conn)
        exit()
    else:
        print("unknown command: '{cmd}'")
