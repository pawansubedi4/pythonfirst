class car:
    price=1000000

    def brand(self,name):
        print(f"this is a {name} car")

    def add(self,a,b):
        return a+b
    
obj=car()
print(obj.price)
obj.brand("bmw")
print(obj.add(12,23))