import sqlite3
conn =sqlite3.connect('nepal.sqlite3')
cursor=conn.cursor()

# def create_table():
#     cursor.execute("""CREATE TABLE IF NOT EXISTS STUDENTS(
#                 ID INTEGER PRIMARY KEY AUTOINCREMENT,
#                 NAME TEXT NOT NULL,
#                 EMAIL TEXT UNIQUE NOT NULL,
#                 ADDRESS TEXT NOT NULL 
                   
#                    )""")
#     conn.commit()


# create_table()

# def insert_value(name,email,address):
#     cursor.execute("""INSERT INTO STUDENTS (NAME,EMAIL,ADDRESS)
#                    VALUES(?,?,?)""",(name,email,address))
#     conn.commit()
#     print("record inserted successfully")

# name1=input("enter name")
# email1=input("enter email")
# address1=input("enter address")
# insert_value(name1,email1,address1)


# def show_data():
#     cursor.execute("""SELECT * FROM STUDENTS""")
#     # data=cursor.fetchall()
#     data1= cursor.fetchone()
#     # data2=cursor.fetchmany(2)
#     # print(data)
#     print(data1)
#     # print(data2)


# show_data()


# def del_data(id):
#     cursor.execute("""DELETE FROM STUDENTS WHERE ID=?""",(id,))
#     conn.commit()
#     print("students deleted successfully")


# del_data(1)


def update_12(name,address,id):
    cursor.execute("""UPDATE STUDENTS SET NAME= ?,ADDRESS= ? WHERE ID= ?""",(name,address,id))
    conn.commit()
    print("students updated successfully")



update_12("harihar","chitwan",4)


