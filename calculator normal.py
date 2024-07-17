import tkinter as tk
app = tk.Tk()
app.title("calculater")
app.geometry("300x400")

first_Label = tk.Label(app, text="enter first no")
first_Label.pack()
firstNumber=tk.Entry(app)
firstNumber.pack()
second_Label = tk.Label(app, text="enter second no")
second_Label.pack()
secondNumber=tk.Entry(app)
secondNumber.pack()
third_Label = tk.Label(app, text="for squar and cube enter only on 1st no")
third_Label.pack()

result = tk.Label(app, text="result")
result.pack()
def add():
    n1=int(firstNumber.get())
    n2=int(secondNumber.get())
    result.config(text=f"result: {n1+n2}")
def sub():
    n1=int(firstNumber.get())
    n2=int(secondNumber.get())
    result.config(text=f"result: {n1-n2}")
def mun():
    n1=int(firstNumber.get())
    n2=int(secondNumber.get())
    result.config(text=f"result: {n1*n2}")
def div():    
    n1=int(firstNumber.get())
    n2=int(secondNumber.get())
    result.config(text=f"result: {n1/n2}")
def sqr():    
    n1=int(firstNumber.get())
    result.config(text=f"result: {n1*n1}")  
def cub():    
    n1=int(firstNumber.get())
    result.config(text=f"result: {n1*n1*n1}")



button = tk.Button(app,text="x",command=mun)
button.pack()
button = tk.Button(app,text="/",command=div)
button.pack()

button = tk.Button(app,text="squar",command=sqr)
button.pack()
button = tk.Button(app,text="cube",command=cub)
button.pack()



button = tk.Button(app,text="+",command=add)
button.pack()
button = tk.Button(app,text="-",command=sub)
button.pack()
app.mainloop()


