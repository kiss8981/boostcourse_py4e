import datetime
import calendar

def get_dats(y, m, d):
    days = ["월","화","수","목","금","토","일"]
    return days[calendar.weekday(y, m, d)]


def after_100(y, m, d):
    day = datetime.datetime(y,m,d)
    day_100 = day + datetime.timedelta(days=100)
    print(f"{day} 의 100 일뒤는 {day_100.year}년 {day_100.month}월 {day_100.day}일 {get_dats(day_100.year, day_100.month, day_100.day)} 입니다")


after_100(2021,6,21)
after_100(2021,6,22)
after_100(2021,6,23)
after_100(2021,6,24)