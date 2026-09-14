def is_disarium(n):
    k = 0
    summ = 0
    for i in str(n):
        k+=1
        summ = summ + int(i)**k
    if n == summ:
        return True
    else:
        return False
is_disarium(89)    # True    8^1 + 9^2 = 8 + 81 = 89
is_disarium(135)   # True    1^1 + 3^2 + 5^3 = 1 + 9 + 125 = 135
is_disarium(564)   # False   5^1 + 6^2 + 4^3 = 105