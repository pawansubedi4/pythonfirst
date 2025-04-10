import tkinter as tk
import tkinter.messagebox as msg
import sqlite3



conn=sqlite3.connect("PAWAN.sqlite3")
c=conn.cursor()


def create_table():
    c.execute("""CREATE TABLE  IF NOT EXISTS STUDENTS(
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            class TEXT,
            address TEXT,
            email TEXT,
            phone TEXT)""")
    conn.commit()
create_table()

APP=tk.Tk()




mainloop.app()

