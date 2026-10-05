def multiplication_table(n):
    y = []
    for i in range(1,11):
        y.append(f"{n} x {i} = {n * i}")
    return y