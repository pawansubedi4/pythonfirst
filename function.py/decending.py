def decend(*x):
    n=list(x)
    t=0
    i=0
    while i<len(n):
        j=i+1
        while j<len(n):
            if n[i]<=n[j]:
                t=n[i]
                n[i]=n[j]
                n[j]=t
            j+=1
        i+=1
    return n


print(decend(65,43,34,23,67,34,56,76,67,67,89,12,12,34,34))




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




def decend(*x):
    n=list(x)
    
    i=0
    while i<len(n):
        j=i+1
        while j<len(n):
            if n[i]<=n[j]:
                n[i]=n[i]-n[j]
                n[j]=n[i]+n[j]
                n[i]=n[j]-n[i]

            j+=1
        i+=1
    return n


print(decend(65,43,34,23,67,34,56,76,67,67,869,12,12,34,34))




def decend(*x):
    n=list(x)
    
    i=0
    while i<len(n):
        j=i+1
        while j<len(n):
            if n[i]<=n[j]:
                n[i]=n[i]^n[j]
                n[j]=n[i]^n[j]
                n[i]=n[j]^n[i]

            j+=1
        i+=1
    return n


print(decend(65,43,34,23,67,34,56,76,67,67,978,12,12,34,34))