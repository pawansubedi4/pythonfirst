import tkinter as tk
app = tk.Tk()
app.title("pawan")
app.geometry("2000x20000")
pawan_Label = tk.Label(app, text="enter first no")
pawan_Label.pack()
firstNumbr=tk.Entry(app)
firstNumbr.pack()
second_Label = tk.Label(app, text="enter second no")
second_Label.pack()
secondNumber=tk.Entry(app)
secondNumber.pack()
result = tk.Label(app, text="result")
result.pack()
def add():
    n1=int(firstNumbr.get())
    n2=int(secondNumber.get())
    result.config(text=f"result: {n1+n2}")
def sub():
    n1=int(firstNumbr.get())
    n2=int(secondNumber.get())
    result.config(text=f"result: {n1-n2}")


button = tk.Button(app,text="+",command=add)
button.pack()
button = tk.Button(app,text="-",command=sub)
button.pack()
app.mainloop()



