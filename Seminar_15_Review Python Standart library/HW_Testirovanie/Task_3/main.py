from datetime import datetime, timedelta


def future_date(change_day):
    local_date = datetime.now()
    time_delta = timedelta(change_day)
    next_date = local_date + time_delta
    future_date = next_date.strftime('%Y-%m-%d')
    print(future_date)


future_date(10)

