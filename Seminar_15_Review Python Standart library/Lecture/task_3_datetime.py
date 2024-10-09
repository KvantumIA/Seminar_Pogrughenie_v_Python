from datetime import time, date, datetime, timedelta

d = date(year=2007, month=6, day=15)
t = time(hour=2, minute=14, second=0, microsecond=24)
dt = datetime(year=2007, month=6, day=15, hour=2, minute=14, second=0,
              microsecond=24)
print(f'{d = }\t-\t{d}')
print(f'{t = }\t-\t{t}')
print(f'{dt = }\t-\t{dt}')

# print()
#
delta = timedelta(weeks=1, days=2, hours=3, minutes=4, milliseconds=6,
                  microseconds=7)
print(f'{delta = }\t-\t{delta}')

print()
#
# delta = timedelta(weeks=53, days=500, hours=73, minutes=101, seconds=303,
#                   milliseconds=67890, microseconds=1234567)
# neg_delta = timedelta(days=-3, minutes=-42)
# print(f'{delta = }\t-\t{delta}')
# print(f'{neg_delta = }\t-\t{neg_delta}')
#
# print()

# date_1 = datetime(2012, 12, 21)
# date_2 = datetime(2017, 8, 19)
# delta = date_2 - date_1
# print(f'{delta = }\t-\t{delta}')
#
# birthday = datetime(1503, 12, 14)
# dlt = timedelta(days=365.25 * 33)
# new_date = birthday + dlt
# print(f'{new_date = }\t-\t{new_date}')
#
# print()

dt = datetime(year=2007, month=6, day=15, hour=2, minute=14, second=0)

print(dt)
print(dt.timestamp())
print(dt.isoformat())
print(dt.weekday())
print(dt.strftime('Дата %d %B %Y. День недели %A. Время %H:%M:%S. Это %W неделя и %j день года.'))

