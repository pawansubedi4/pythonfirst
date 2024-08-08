import sqlite3
conn =sqlite3.connect('nepal.sqlite3')
cursor=conn.cursor()

def create_table():
    cursor.execute("""CREATE TABLE IF NOT EXISTS STUDENTS(
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                NAME TEXT NOT NULL,
                EMAIL TEXT UNIQUE NOT NULL,
                ADDRESS TEXT NOT NULL 
                   
                   )""")
    conn.commit()


create_table()

def insert_value(name,email,address):
    cursor.execute("""INSERT INTO STUDENTS (NAME,EMAIL,ADDRESS)
                   VALUES(?,?,?)""",(name,email,address))
    conn.commit()
    print("record inserted successfully")

name1=input("enter name")
email1=input("enter email")
address1=input("enter address")
insert_value(name1,email1,address1)
