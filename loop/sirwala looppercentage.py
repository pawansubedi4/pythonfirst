num=int(input("enter number of students"))
marks=[]
x=1
while x<=num:
    print(f"====student{x}======")
    nep=int(input("enter marks in nepali"))
    eng=int(input("enter marks in eng"))
    mat=int(input("enter marks in math"))
    sce=int(input("enter marks in science"))
    acc=int(input("enter marks in account"))
    total=nep+eng+mat+sce+acc
    marks.append(total)
    x+=1
for total in marks:
    print("student")
    per=total/5
    print("total:",total)
    print("pertences:",per)
    if per>=80:
        print("distensen")
    elif per>60:
        print("first")  
    elif per>45:
        print("second") 
    elif per>=32:
        print("third") 
    else:
        print("fail")            

