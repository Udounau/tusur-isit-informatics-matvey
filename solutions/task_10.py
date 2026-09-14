def index_of_min(values):
    if values == []:
        print(-1)
    else:
        print(values.index(min(values)))
index_of_min([10, -3, -5, 2, 5])   # 2
index_of_min([1, 2, 3])            # 0
index_of_min([4, 1, 1, 9])         # 1
index_of_min([])                   # -1