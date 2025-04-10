class laptop:
    def brand(self,name):
        print("laptop is brand")

class dell(laptop):
    pass

class mac(laptop):
    pass
obj=dell()
obj.brand("dell")

# 

class mobile:
    def brand(self,name,quantity,price):
        print(f"name={name} quantity={quantity} price={price}")

class apple(mobile):
    pass

class samsung(mobile):
    pass
obj=apple()
obj.brand("pawan",10,124334)

    
    