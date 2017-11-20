#Andrew Parker
#11/17/17
#displayDate.py - gives current date

from datetime import date

today = date.today() 
day = ['Monday','Tuesday','Wednesday','Thursday','Friday']
if today.weekday == 0:
    day = 'Monday'
elif today.weekday == 1:
    day = 'Tuesday'
elif today.weekday == 2:
    day = 'Wednesday'
elif today.weekday == 3:
    day = 'Thursday'
elif today.weekday == 4:
    day = 'Friday'
elif today.weekday == 5:
    day = 'Saturday'
elif today.weekday == 6:
    day = 'Sunday'

print(day)
print(today.month)
print(today.year)