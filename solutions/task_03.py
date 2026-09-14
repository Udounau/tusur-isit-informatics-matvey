def is_divisor(a, b):
    if a == 0:
        return False
    elif b % a == 0:
        return True
    else:
        return False