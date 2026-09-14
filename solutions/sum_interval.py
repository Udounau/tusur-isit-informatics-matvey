def sum_interval(a, b):
    k = 0
    if a > b:
          for i in range(b, a):
            k+=1
    else:
        for i in range(a, b+1):
            k+=i
    return k
