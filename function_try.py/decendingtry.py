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


