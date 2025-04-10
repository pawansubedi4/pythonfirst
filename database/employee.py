import sqlite3
conn =sqlite3.connect('nepal.sqlite3')
cursor=conn.cursor()

def emp_table():
    cursor.execute("""CREATE TABLE IF NOT EXISTS employee_data(
                EMP_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                EMP_NAME TEXT NOT NULL,
                EMP_EMAIL TEXT UNIQUE NOT NULL,
                EMP_ADDRESS TEXT NOT NULL,
                EMP_PHONE TEXT  
                   
                   )""")
    conn.commit()


emp_table()

def insert_value(name,email,address,phone=0):
    cursor.execute("""INSERT INTO employee_data (EMP_NAME,EMP_EMAIL,EMP_ADDRESS,EMP_PHONE)
                   VALUES(?,?,?,?)""",(name,email,address,phone))
    conn.commit()
    print("record inserted successfully")

name1=input("enter name")
email1=input("enter email")
address1=input("enter address")
phone1=input("enter phone number")
insert_value(name1,email1,address1,phone1)
# insert_value("RAM","HARI","SHYAM","836534786")

