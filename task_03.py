def is_divisor(a, b):
    if a == 0:
        print("False")
    elif b % a == 0:
        print("True")
    else:
        print("False")
is_divisor(3, 12)   # True
is_divisor(5, 12)   # False
is_divisor(0, 12)   # False
is_divisor(7, 0)    # True