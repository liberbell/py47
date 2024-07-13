import datetime

today = datetime.date.today()
print(today.year, today.month, today.day)
yesterday = today - datetime.timedelta(days=1)
print(yesterday)
print(today.strftime("%Y/%m/%d"))
print(datetime.datetime.now())