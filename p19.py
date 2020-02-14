import datetime

base = datetime.datetime.fromisoformat('1901-01-01')
end_date = datetime.datetime.fromisoformat('2000-12-31')
cur_date = base

sundays = 0
while cur_date != end_date:
    if cur_date.weekday() == 6 and cur_date.day == 1:
        sundays += 1
        print(cur_date, cur_date.strftime('%A'), sundays)
    cur_date += datetime.timedelta(days=1)

print(sundays)