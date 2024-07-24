print("=====================computer bazar=================")
print("1. dell (rs 20000) 2. toshiba (rs 30000) 3.mac(rs : 50000)")
dell_price=0
tosiba_price=0
mac_price=0
product_name=0
quantity=0
 
option=int(input("enter the option"))
if option==1:
    quantity=int(input("enter the quantity"))
    dell_price=20000*quantity
    product_name="dell"
elif option==2:
    quantity=int(input("enter the quantity"))
    tosiba_price=30000*quantity
    product_name="tosiba"
elif option ==3:
    quantity=int(input("enter the quantity"))
    mac_price=50000*quantity
    product_name="mac"
else:
    print("not in option")

delevary_price=0
print("1.home(rs1000) 2. pickup(rs0)")
del_option=int(input("enter option"))
if del_option==1:
    delevary_price=1000
packing_charge=0
print("1.plastic (rs 100) 2.bag(rs 400)  3.giftbox (rs 1000)")
pack_option=int(input("enter option"))
if pack_option==1:
    packing_charge=100
elif pack_option==2:
    packing_charge=400
elif pack_option==3:
    packing_charge=1000


print("location: 1.ktm  2.lalitpur 3.bhakatapur")
tto=dell_price+tosiba_price+mac_price
tax_amt=0
location=int(input("enter option"))
if location==1:
    tax_amt=tto*0.13

total=tto+delevary_price+packing_charge+tax_amt
print("============bill=======")
print(f"product name ={product_name}")
print("quantity = ",quantity)
print("total=",tto)
print("delevary charge",delevary_price)
print("packing charge",packing_charge)
print("tax amount=",tax_amt)
print("grand total =",total)
print("thanks for using it")


