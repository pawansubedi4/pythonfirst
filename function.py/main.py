# what is function
# build in funcrion eg len(),print(), input()



def greet():
    print("hello world")

greet()


def add (x,y):
    print(x+y)

add(10,20)


# result(name, nepali englkish math science sociasl)
name1=input("enter your name")
m1=int(input("enter your marks in 1st subject "))
m2=int(input("enter your marks in 1st subject "))
m3=int(input("enter your marks in 1st subject "))
m4=int(input("enter your marks in 1st subject "))
m5=int(input("enter your marks in 1st subject "))

def result():
    sum=m1+m2+m3+m4+m5
    tt=int(input("enter your total marks "))
    per=sum/tt*100
    print("the result of ",name1)
    if per>90:
        print("A+")
    elif per>80 and per<90:
        print("A")   
    elif per>70 and per<80:
        print("B+")
    elif per>60 and per<70:
        print("B")
    elif per>50 and per<60:
        print("C+")
    elif per>40 and per<50:
        print("C")
    elif per>35 and per<40:
        print("D+")
    else:
        print("fail")  
result()    




