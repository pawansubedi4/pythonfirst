no=int(input("enter the no of student "))
marks=[]
for x in range(no):
    print(f"========student{}")
    total=0
    for y in range(5):
        marks=int(input("enter no on subject"))
        
        
    
        total+=marks
    
    print("total=",total)
    per=total/500*100
    print("percentage=",per)