class students:

    def __init__(self,name):
        print(f"my name is {name}")
    def info(self):
        print("this is info method")

    def __del__(self):
        print("it is ended")
    

obj=students("ram")
obj.info()

# __str__
# __repr__
# __add__

