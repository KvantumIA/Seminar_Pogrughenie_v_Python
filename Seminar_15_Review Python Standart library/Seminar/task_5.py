"""
Дорабатываем задачу 4.
Добавьте возможность запуска из командной строки.
При этом значение любого параметра можно опустить. В
этом случае берётся первый в месяце день недели, текущий
день недели и/или текущий месяц.

*Научите функцию распознавать не только текстовое
названия дня недели и месяца, но и числовые,
т.е не мая, а 5.
"""
import argparse
from datetime import datetime

WEEK = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота',
        'воскресенье']


def is_leap(year):
    return bool(not year % 4 and year % 100 or not year % 400)


def months(year=2000):
    return {1: ('янв', 31), 2: ('фев', 29 if is_leap(year) else 28),
            3: ('мар', 31),
            4: ('апр', 30), 5: ('мая', 31), 6: ('июн', 30), 7: ('июл', 31),
            8: ('авг', 31),
            9: ('сен', 30), 10: ('окт', 31), 11: ('ноя', 30), 12: ('дек', 31)}


# 3-я среда июля
def parse_date(date_txt):
    year = datetime.now().year
    temp_date = months(datetime.now().year)
    month = datetime.now().month
    week = str(datetime.strptime(f'01.{month}.{year}', '%d.%m.%Y').weekday() + 1)
    weekday = datetime.strptime(f'01.{month}.{year}', '%d.%m.%Y').weekday()
    try:
        date = date_txt.split()
        if len(date) < 3:
            for item in date:
                if item in WEEK:
                    weekday = item
                elif item not in WEEK and len(item.split('-')) <= 1:
                    for i, m in temp_date.items():
                        if item[:3] == m[0]:
                            month = i
                            week = str(datetime.strptime(f'01.{month}.{year}',
                                                         '%d.%m.%Y').weekday() + 1)
                            weekday = datetime.strptime(f'01.{month}.{year}',
                                                        '%d.%m.%Y').weekday()
                elif len(item.split('-')) > 1:
                    week = item[0]
        else:
            week, weekday, month = date_txt.split()
    except:
        raise ValueError

    if isinstance(week, list):
        if not (week[0].isdigit() and 0 < int(week[0]) < 6):
            raise ValueError
    if isinstance(weekday, str) and not weekday.isdigit():
        if weekday not in WEEK:
            raise ValueError
        for i, m in temp_date.items():
            if month[:3] == m[0]:
                return int(week[0]), weekday, i
        return int(week[0]), weekday, month
    elif isinstance(weekday, int) or weekday.isdigit():
        if not ((0 < int(weekday) - 1) < len(WEEK)):
            raise ValueError
        return int(week[0]), int(weekday), int(month)


def check_date(text_date):
    week, weekday, month = parse_date(text_date)
    year = datetime.now().year
    first_day_of_month = datetime.strptime(f'01.{month}.{year}',
                                           '%d.%m.%Y').weekday()
    current_week = WEEK[first_day_of_month:] + WEEK[:first_day_of_month]
    temp_date = months(datetime.now().year)
    if isinstance(weekday, int) or weekday.isdigit():
        for i in range(int(temp_date[int(month)][1])):
            if weekday == 7:
                weekday -= 1
            if WEEK[int(weekday)] == current_week[i % 7]:
                week -= 1
                if not week:
                    return f'{i + 1}.{months(year)[int(month)][0]}.{year}'
        raise ValueError
    for j in range(months(year)[int(month)][1]):
        if weekday == current_week[j % 7]:
            week -= 1
            if not week:
                return f'{j + 1}.{months(year)[int(month)][0]}.{year}'
    raise ValueError


text_date1 = '4-я суббота июня'
text_date2 = '4-я 7 7'
text_date3 = '2-я'
text_date4 = 'августа'
text_date5 = '3-я пятница января'
# print(check_date(text_date1))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Определение даты по заданному описанию.')
    parser.add_argument('date_description', type=str, nargs='?', default=text_date5,
                        help='Описание даты (например, "3-я пятница мая" или "2-я 3 5")')

    args = parser.parse_args()

    try:
        result = check_date(args.date_description)
        print(f'Дата: {result}')
    except ValueError as e:
        print(f'Ошибка: {e}')
