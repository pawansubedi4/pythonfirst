import tkinter as tk
import tkinter.messagebox as msg
import sqlite3
conn =sqlite3.connect('database.sqlite3')
cursor=conn.cursor()

def create_table():
    cursor.execute("""CREATE TABLE IF NOT EXISTS user_data(
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                NAME TEXT NOT NULL,
                EMAIL TEXT UNIQUE NOT NULL,
                ADDRESS TEXT NOT NULL,
                PHONE TEXT  
                   
                   )""")
    conn.commit()
create_table()


app=tk.Tk()
app.title("my gui app")
app.geometry("500x500")
first_leble=tk.Label(app,text="enter recordes of yours ")
first_leble.grid(row=0,column=2)

second_leble=tk.Label(app,text="name")
second_leble.grid(row=1,column=0)
name=tk.Entry(app)
name.grid(row=1,column=1)

fourth_leble=tk.Label(app,text="gmail")
fourth_leble.grid(row=3,column=0)
gmail=tk.Entry(app)
gmail.grid(row=3,column=1)

fift_leble=tk.Label(app,text="address")
fift_leble.grid(row=4,column=0)
address=tk.Entry(app)
address.grid(row=4,column=1)

sixth_leble=tk.Label(app,text="phone number")
sixth_leble.grid(row=5,column=0)
phone=tk.Entry(app)
phone.grid(row=5,column=1)


def add_record():
    fname=name.get()
    gmails=gmail.get()
    addresss=address.get()
    phones=phone.get()
    cursor.execute("""INSERT INTO user_data(NAME,EMAIL,ADDRESS,PHONE) VALUES(?,?,?,?) """,(fname,gmails,addresss,phones))
    conn.commit()
    name.delete(0,tk.END)
    gmail.delete(0,tk.END)
    address.delete(0,tk.END)
    phone.delete(0,tk.END)
    msg.showinfo("record added","records added successfully")


def delete_data():
    sixth_leble=tk.Label(app,text="name to delete")
    sixth_leble.grid(row=8,column=0)
    deletei=tk.Entry(app)
    deletei.grid(row=8,column=1)
    delete1=deletei.get()
    deletei.delete(0,tk.END)

    return delete1
def delete_hai():
    delete2=delete_data()
    delete3= int(delete2)
    print(type(delete3))
    cursor.execute("""DELETE FROM user_data WHERE ID=?""",(delete3,))
    conn.commit()
    msg.showinfo("data deleted","data deleted successfully")


button=tk.Button(app,text="conform delete",command=delete_hai)
button.grid(row=9,column=0,columnspan=2)


    



button=tk.Button(app,text="add record",command=add_record)
button.grid(row=6,column=0,columnspan=2)





app.mainloop()
