import datetime

LOCAL_TIMEZONE = datetime.datetime.now(
    datetime.timezone(datetime.timedelta(0))
).astimezone()

DATE = datetime.datetime.strftime(LOCAL_TIMEZONE, '%Y-%m-%d')