# use_datetime.py
# -*- coding: utf-8 -*-

from datetime import datetime, timedelta,  timezone

# now = datetime.now()
# print(now)
# dt = datetime(2015, 4, 19, 12, 20)
# print(dt.timestamp())

# t = 1429417200.0
# print(datetime.utcfromtimestamp(t))

# cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
# print(cday)

# now = datetime.now()
# print(now.strftime('%a, %b %d %H:%M'))

tz_utc_8 = timezone(timedelta(hours=8))
now = datetime.now()
print(now)

dt = now.replace(tzinfo=tz_utc_8)
print(dt)