# optional parameter

def user (name,age=0):
    print(name)
    print(age)


user("ram",50)
user("sita")


# lamda function
total=lambda x,y: x+y
print(total(10,20))


# recurtion function

def fact(n):
    if n==1:
        return 0
    else:
        return n*fact(n-1)
print(fact(5))


# global variable and lockal variable
# global
x=10
def test():
    print(x)

