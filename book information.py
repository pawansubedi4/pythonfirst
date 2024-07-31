obj =open("name.txt","a")
name =input("enter book name")
auther =input("enter auther name")
year=input("enter prented year")
quantity=input("enter quantity")
obj.write(f"{name}\t{auther}\t{year}\t{quantity}\n")
obj.close()


obj=open("name.txt","r")
for name in obj.readlines():
    print(name)


