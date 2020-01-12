import calendar

calendar.setfirstweekday(6) # If you comment this out the weekday starts on Monday

print(calendar.weekheader(3)) # 
print()

print(calendar.month(2020, 1))
print()

print(calendar.calendar(2020))
print()

day_of_the_week = calendar.weekday(1974, 4, 21)
print(day_of_the_week)
print()

print(calendar.monthrange(2020, 11))

