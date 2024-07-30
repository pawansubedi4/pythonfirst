print("=======BOOK shop=========")
print("1.muna madan (rs 1000) \n2.yeak chayan (rs 800) \n3. the reason of the reavel (rs 1500)")
hi=int(input("enter which book you want"))
muna_price,yeak_price,reavel_price,quantity,book_name=0,0,0,0,""

if hi==1:
    quantity=int(input("enter quantity how much do you want"))
    muna_price=1000*quantity
    book_name="muna madan"
elif hi ==2:
    quantity=int(input("enter quantity how much do you want"))
    yeak_price=800*quantity
    book_name="yeak chayan"
elif hi==3:
    quantity=int(input("enter quantity how much do you want"))
    reavel_price=1500*quantity
    book_name="the reasion of the reavel"            
else:
    print("it is not in option")
del_price=0
tax_price=0
print("delevary options are") 
print("1.within a town (rs 80) \n 2.within a country (rs 400) 3.outside country (rs 2000")
del_option=int(input("enter which option you want"))   
if del_option==1:
    del_price=80
elif del_option==2:
    del_price=400
elif del_option==3:
    del_price=2000
else:
    print("not in option")
tax_total=muna_price+yeak_price+reavel_price
tax_price=float(tax_total*0.13)
grand_total=tax_total+del_price+tax_price  
print("................bill............")
print(f"product name = {book_name}")
print("product price=",tax_total)
print("delevary charge=",del_price)
print("tax amount=",tax_price)
print(f"grand total {grand_total}")

              

