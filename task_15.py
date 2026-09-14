def days_in_month(month, year):
    u = 0
    y = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if year % 4 == 0 and month == 2:
        if year % 100 != 0 or year % 400 == 0:
            u = 1
            print("29")
    if u == 0:
        print(y[month-1])
days_in_month(1, 2001)    # 31
days_in_month(2, 2001)    # 28
days_in_month(2, 2000)    # 29
days_in_month(2, 1900)    # 28
days_in_month(11, 2025)   # 30