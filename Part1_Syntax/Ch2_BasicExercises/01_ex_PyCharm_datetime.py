# 오늘 날짜 출력

import datetime

today = datetime.datetime.today()
print(today)
# print(today.year)
# print(today.month)
# print(today.day)
# print(today.weekday())
# print(today.hour)
# print(today.minute)
# print(today.second)
weekday = today.weekday()
if weekday == 0:
    weekday = '월'
elif weekday == 1:
    weekday = '화'
elif weekday == 2:
    weekday = '수'
elif weekday == 3:
    weekday = '목'
elif weekday == 4:
    weekday = '금'
elif weekday == 5:
    weekday = '토'
elif weekday == 6:
    weekday = '일'

print('{}년 {}월 {}일 {}요일'.format(today.year, today.month, today.day, weekday))
print('{}시 {}분 {}초'.format(today.hour, today.minute, today.second))

date = datetime.datetime.date(today)
time = datetime.datetime.time(today)
print(date.strftime('%y/%m/%d'))
print(time.strftime('%h:%m:%S'))  # '%s'로 소문자를 쓰면 ValueError: Invalid format string~!
print(today.strftime('%y/%m/%d %H:%M:%S'))
