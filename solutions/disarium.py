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