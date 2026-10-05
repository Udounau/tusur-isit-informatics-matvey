def is_power_of_two(n):
    if bin(n)[2:].count("1") == 1:
        return True
    else:
        return False