import datetime


# 1. Get current date and time

x = datetime.datetime.now()
print(x)


# 2. Create a date object

x = datetime.datetime(2020, 5, 17)
print(x)


# 3. Access year and weekday

x = datetime.datetime(2020, 5, 17)
print(x.year)
print(x.strftime("%A"))


# 4. Format date

x = datetime.datetime(2018, 6, 1)
print(x.strftime("%B"))


# 5. Time difference

x = datetime.datetime(2020, 5, 17)
y = datetime.datetime(2020, 5, 20)

print(y - x)