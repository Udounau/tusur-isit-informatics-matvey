def compare(m, n):
    if m > n:
        print("Number m > n")
    if n < m:
        print("Number m < n")
    if n == m:
        print("The numbers are equal")
compare(5, 3)   # 'Number m > n'
compare(3, 5)   # 'Number m < n'
compare(4, 4)   # 'The numbers are equal'