ln=int(input("enter how much did you enter"))
n=[]
for a in range(ln):
    n.append(int(input("enter no")))
    



def decend(*an):
    an=list(n)
    for i in range(len(an)):
        for j in range(i+1,len(an)):
            if an[i]<=an[j]:
                an[i],an[j]=an[j],an[i]   
    return an
# print(decend(80,70,30,40,50,60,1234567,234567,87654,34567,7654))
# print(decend(int(input("number"))))
print(decend(n))




