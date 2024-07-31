# main types of function
def pr(data):
    print(data)

pr("hello")
pr(34)
pr(34.5) 


def multi(num):
    for i in range(1,11):
        print(f"{num} X {i} = {num*i}")



multi(5)



def user(name,age):
    print(name)
    print(age)

user("ram",12)


def user1(name,age=0):  #optional argument chai pachadi huncha hai
    print(name)
    print(age)



user1("ram")


def student(*name):
    print(name)

student("ram","sita","hari")


a,*b=10,20,30,40
print(a)
print(b)

def student(*name,**data): #** or keyword argument pachadi nai huna parcha
    print(name)
    print(data)

student("ram","sita","hari",name="hari",rollno=10)


def total(*num):
    sm=0
    for i in num:
        sm+=i
    return sm
print(total(1,2,3,4,5,6,7,8))

#memory location of function
def text():
    pass

print(text())




def add(x,y):
    return x+y

total=add   # we cant do add()
print(total(10,20))



# lambda function
total=lambda x,y:x+y
print(total(10,20))


# recurtion function()

def fact(n):
    if n==1 or n==0:
        return 1
    else:

        return n*fact(n-1)
print(fact(5))



#global variable
x=10   # it can be call fron anwhere
def test():
    y=18  # local variable   it cant be call outside the function
    print(x)
    print(y)
text()
print(x)

# but cant print(y)

# to make global variable inside function 
def hehe():
    global x
    x=x+30
    print(x)

hehe()


def total2(x,y):

    return x+y

def add1(x,y,callback):  # callback can be anything
    print(callback(x,y))

add1(10,20,total2)



# nexted function

def outer():
    def inner():
        print("hello pawan")



def outer():
    def inner():
        return "hello"
    return inner
print(outer())
a= outer()
print(a())