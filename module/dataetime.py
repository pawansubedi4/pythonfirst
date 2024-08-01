import datetime


s=[
    {'title':'python developer','salary':20000,'exp_date':'2023-08-3'},
    {'title':'java developer','salary':30000,'exp_date':'2022-08-3'},
    {'title':'c# developer','salary':25000,'exp_date':'2021-08-3'},
    {'title':'c++ developer','salary':40000,'exp_date':'2024-09-3'},
    {'title':'php developer','salary':15000,'exp_date':'2024-08-13'},
]
today_date=datetime.datetime.today()

print(today_date)

for job in range(5):
    exp=datetime.datetime.strptime(s[job]['exp_date'],'%Y-%m-%d')
    
    if exp<today_date:
        exp_days=today_date-exp
        print(f"{s[job]["title"]} date was expired {exp_days} days ago ")
    else:
        exp_days=exp-today_date
        print(f"{s[job]["title"]} date was not  expired it will expired in {exp_days} days")
