def input_marks():
    
    m1=int(input("enter your marks in 1st subject "))
    m2=int(input("enter your marks in 1st subject "))
    m3=int(input("enter your marks in 1st subject "))
    m4=int(input("enter your marks in 1st subject "))
    m5=int(input("enter your marks in 1st subject "))
    return [m1,m2,m3,m4,m5]

def tot():
    m1,m2,m3,m4,m5 = input_marks()
    return m1+m2+m3+m4+m5


def perc():
    total1= tot()
    per=total1/500*100
    return per,total1


def division():
    per,total1 = perc()
    
    if per>90:
        return ("A+",total1)
    elif per>80 and per<90:
        return("A",total1)   
    elif per>70 and per<80:
        return("B+",total1)
    elif per>60 and per<70:
        return("B",total1)
    elif per>50 and per<60:
        return("C+",total1)
    elif per>40 and per<50:
        return("C",total1)
    elif per>35 and per<40:
        return("D+",total1)
    else:
        return("fail",total1)  
    

def display():
    div,total1=division()
#    return div,total1
    print(f"the total is {total1} and the division is {div}")


# print(display())  
display()

