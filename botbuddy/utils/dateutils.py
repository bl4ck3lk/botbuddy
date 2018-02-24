import datetime as dt


def get_n_days_ago(n):
    return str(dt.date.today() - dt.timedelta(days=n))
