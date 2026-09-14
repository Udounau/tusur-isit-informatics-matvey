def multiplication_table(n):
    y = []
    for i in range(1,11):
        y.append(f"7 x {i} = {n * i}")
    print(y)
multiplication_table(7)