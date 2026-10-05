def days_in_month(month, year):
    u = 0
    y = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if year % 4 == 0 and month == 2:
        if year % 100 != 0 or year % 400 == 0:
            u = 1
            return 29
    if u == 0:
        return int(y[month-1])