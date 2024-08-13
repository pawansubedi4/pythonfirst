class calculator:
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def multi(self,a,b):
        return a*b
    def div(self,a,b):
        return a/b
    def rem(self,a,b):
        return a%b
obj=calculator()
print(obj.add(12,23))
print(obj.sub(23,12))
print(obj.multi(12,3))
print(obj.div(12,3))
print(obj.rem(13,2))