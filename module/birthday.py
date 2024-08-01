import datetime
today_date=datetime.datetime.today()
birthday="2004-9-1"
birthday_date=datetime.datetime.strptime(birthday,'%Y-%m-%d')
print(birthday_date)
print(today_date)
today=today_date.month
todayday=today_date.day
birth=birthday_date.month
birthday=birthday_date.day
if today>birth:
    if todayday>birthday:
        diff_month=today-birth
        diff_day=todayday-birthday
        print(f"your birthday id passsed {diff_month}and {diff_day}")
    elif todayday==birthday:
        diff_month=today-birth
        
        print(f"your birthday id passsed {diff_month} month ago")
    else:
        diff_month=today-birth-1
        diff_day=30-(birthday-todayday)
        print(f"your birthday id passsed {diff_month}and {diff_day}")



    
    
elif today==birth:
    if todayday>birthday:
    
        diff_day=todayday-birthday
        print(f"your birthday id passsed {diff_day}")
    elif todayday==birthday:

        print(f"your birthday is today happy birthday")
    else:
    
        diff_day=birthday-today
        print(f"your birthday is comming {diff_day}")
    
else:  # today<birth
    if todayday>birthday:
        diff_month=birth-today-1
        diff_day=30-(todayday-birthday)
        print(f"your birthday id comming {diff_month}and {diff_day}")
    elif todayday==birthday:
        diff_month=birth-today
        
        print(f"your birthday id comming {diff_month}")
    else:
        diff_month=birth-today
        diff_day=birthday-todayday
        print(f"your birthday id comming {diff_month}and {diff_day}")
