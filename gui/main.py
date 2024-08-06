import tkinter as tk
import tkinter.messagebox as msg
app=tk.Tk()
app.title("my gui app")
app.geometry("500x500")
first_leble=tk.Label(app,text="enter recordes of yours ")
first_leble.grid(row=0,column=2)
second_leble=tk.Label(app,text="first name")
second_leble.grid(row=1,column=0)
firstName=tk.Entry(app)
firstName.grid(row=1,column=1)
third_leble=tk.Label(app,text="last name")
third_leble.grid(row=2,column=0)
lastName=tk.Entry(app)
lastName.grid(row=2,column=1)
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
    with open("records.txt","a") as file:
        fname=firstName.get()
        lname=lastName.get()
        gmails=gmail.get()
        addresss=address.get()
        phones=phone.get()
        file.write(f"first name={fname}\t second name={lname}\t gmail={gmails} \t address={addresss}\tphone={phones}\n")
        # fname.delete(0,tk.end)
        # lname.delete(0,tk.end)
        # gmails.delete(0,tk.end)
        # addresss.delete(0,tk.end)
        # phones.delete(0,tk.end)
        msg.showinfo("record added","records added successfully")



button=tk.Button(app,text="add record",command=add_record)
button.grid(row=6,column=0,columnspan=2)




app.mainloop()