def sum_interval(a, b):
    k = 0
    if a > b:
          for i in range(b, a):
            k+=1
    else:
        for i in range(a, b+1):
            k+=i
    print(k)
sum_interval(1, 0)    # 1    1 + 0
sum_interval(1, 2)    # 3    1 + 2
sum_interval(-1, 2)   # 2    -1 + 0 + 1 + 2
sum_interval(5, 5)    # 5