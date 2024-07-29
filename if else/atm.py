print("atm")
pin=int(input("enter your pin: "))
if pin==1234:
    print("welcom to atm")
    print("1.check balance")
    print("2.withdraw money")
    amount=10000
    option=int(input("enter your option"))
    if option==1:
        print("your balance is ",amount)
    elif option==2:
        new_amount =int(input("enter the amt to withdraw"))
        if new_amount>amount:
            print("insufficent balance")
        else:
            rem=amount-new_amount
            print("withdraw amt is",new_amount ) 
            print("remanning is ",rem)
    else:
        print("invalid option")
else:
    print("invalid pin")

