def square_digits(n):
    string = ""
    for i in str(n):
        string = string + str(int(i)**2)
    return string
square_digits(3212)   # 9414
square_digits(2112)   # 4114
square_digits(0)      # 0
square_digits(999)    # 818181
square_digits(10001)  # 10001