import datetime

x = datetime.datetime.now()
print(x)
#return year and weekday
print(x.year)
print(x.strftime("%w"))
print(x.strftime("%B")) #month
print(x.strftime("%A"))
print(x.strftime("%d"))


# creating date objects
d = datetime.datetime(2025,5,10)
print(d)