import datetime
today_date=datetime.datetime.today()
birthday="2004-10-5"
birthday_date=datetime.datetime.strptime(birthday,'%Y-%m-%d')
print(birthday_date)
print(today_date)
today=today_date.month
todayday=today_date.day
birth=birthday_date.month
birthday=birthday_date.day
if today>birth:
    
    print("your birthday is passed")
elif today==birth:
    print("your birthday month")
else:
    print("your birthday is comming")

