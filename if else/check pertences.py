m1=int(input("enter your marks in 1st subject "))
m2=int(input("enter your marks in 1st subject "))
m3=int(input("enter your marks in 1st subject "))
m4=int(input("enter your marks in 1st subject "))
m5=int(input("enter your marks in 1st subject "))
sum=m1+m2+m3+m4+m5
tt=int(input("enter your total marks "))
per=sum/tt*100
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
