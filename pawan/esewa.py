import tkinter as tk
app=tk.Tk()
app.title("esewa") 
app.geometry("400x400")
vfirst_Label=tk.Label(app, text="welocome to esewa")
vfirst_Label.pack()
first_Label=tk.Label(app, text="enter your id ")
first_Label.pack()
id=tk.Entry(app)
id.pack()
second_Label=tk.Label(app, text="password ")
second_Label.pack()
passs=tk.Entry(app)
passs.pack()

id1=9765597688
pass1="pawansubba"


def dis():  
    nid1=int(id.get())
    npass1=passs.get()
    if id1==nid1:
        if npass1==pass1:
           result.config(text=f"{"login in successfull"}")

        else:
            result.config(text=f"{"incorrect password"}")
    
    else:
        result.config(text=f"{"incorrect id"}")
  
button = tk.Button(app,text="Login",command=dis)
button.pack()   
result = tk.Label(app, text="")
result.pack()          
app.mainloop()
