class product:
    product_list=[
        {'name':'apple','price':100},
        {'name':'banana','price':50},
        {'name':'orange','price':150},
        {'name':'graps','price':250}

    ]

    def show_product(self):
        print(self.product_list)

    def add_product(self,name,price):
        data ={'name':name,'price':price}
        self.product_list.append(data)
        self.show_product()

    def delete(self,name):
        for i in range(len(self.product_list)):
            if self.product_list[i]["name"]==name:
                x=list(self.product_list[i])
                x.remove()
                





        





obj=product()
# obj.add_product("cherry",120)
# obj.show_product()
obj.delete("pawan")

