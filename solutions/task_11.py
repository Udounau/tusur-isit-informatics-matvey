def guests_by_seat(seats):
    y = []
    t = False
    n = 1
    for i in range(1,len(seats)+1):
        y.append(seats.index(i)+1)
    return (y)