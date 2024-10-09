"""
Функция получает на вход текст вида: “1-й четверг ноября”, “3-
я среда мая” и т.п.
Преобразуйте его в дату в текущем году.
Логируйте ошибки, если текст не соответсвует формату.
"""
import datetime

# WEEK = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота',
#         'воскресенье']
# MONTH = ['январь', 'февраль', 'март', 'апрель', 'мая', 'июнь', 'июль',
#          'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
# MONTH = [item[:3] for item in MONTH]
#
#
# def parse_date(text_date):
#     week, week_day, month_date = text_date.split()
#     week = int(week[0])
#     month_date = month_date[:3]
#     year = datetime.datetime.now().year
#     week_num = WEEK.index(week_day)  # день недели
#     month_num = MONTH.index(month_date) + 1  # месяц
#     print(f'{week}  {week_num}, {month_num} {year}')
#     first_day_of_month = datetime.datetime.strptime(f'01.{month_num}.{year}',
#                                                     '%d.%m.%Y').weekday()   # день недели
#     print(WEEK[first_day_of_month], first_day_of_month)
#
#     while True:
#         if week_num == first_day_of_month:
#             break
# 2-я среда
#
# text_date1 = '1-й четверг ноября'
# text_date2 = '3-я среда мая'
#
# parse_date(text_date1)
# parse_date(text_date2)


from datetime import datetime

WEEK = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота',
        'воскресенье']


def is_leap(year):
    return bool(not year % 4 and year % 100 or not year % 400)


def months(year=2000):
    return (('янв', 31), ('фев', 29 if is_leap(year) else 28), ('мар', 31),
            ('апр', 30), ('мая', 31), ('июн', 30), ('июл', 31), ('авг', 31),
            ('сен', 30), ('окт', 31), ('ноя', 30), ('дек', 31))


# 3-я среда июля
def parse_date(date_txt):
    try:
        week, weekday, month = date_txt.split()
    except:
        raise ValueError
    if not (week[0].isdigit() and 0 < int(week[0]) < 6):
        raise ValueError
    if weekday not in WEEK:
        raise ValueError
    for i, m in enumerate(months(), 1):
        if month[:3] == m[0]:
            return int(week[0]), weekday, i
    raise ValueError


def check_date(text_date):
    week, weekday, month = parse_date(text_date)
    year = datetime.now().year
    first_day_of_month = datetime.strptime(f'01.{month}.{year}','%d.%m.%Y').weekday()
    current_week = WEEK[first_day_of_month:] + WEEK[:first_day_of_month]
    for i in range(months(year)[month - 1][1]):
        if weekday == current_week[i % 7]:
            week -= 1
            if not week:
                return f'{i + 1}.{months(year)[int(month)-1][0]}.{year}'
    raise ValueError


text_date = '1-я воскресенье июля'

print(check_date(text_date))
