from datetime import datetime

date = datetime.now()
local_date = date.strftime('%Y-%m-%d %H:%M:%S')

day = date.strftime('%A')
week_year = date.isocalendar()[1]


print(local_date)
print(day)
print(week_year)
