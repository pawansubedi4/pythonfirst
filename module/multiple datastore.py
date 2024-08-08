import datetime
num=int(input("enter how many no of studdent data youwant to store"))

for i in range(0,num):
    name=input("enter name")
    birthday=input("enter your date of birth in year-month-day format")
    birth=datetime.datetime.strptime(birthday,'%Y-%m-%d')
    today=datetime.datetime.today()
    lit="1824-10-10"
    limit=datetime.datetime.strptime(lit,'%Y-%m-%d')
    if birth<today and birth>limit:
        print(name,birthday)
print("thankyou for using it")




