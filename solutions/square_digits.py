def square_digits(n):
    string = ""
    for i in str(n):
        string = string + str(int(i)**2)
    return int(string)