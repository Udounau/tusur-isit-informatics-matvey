def is_power_of_two(n):
    if bin(n)[2:].count("1") == 1:
        return True
    else:
        return False
is_power_of_two(1)      # True    2^0
is_power_of_two(1024)   # True
is_power_of_two(4096)   # True
is_power_of_two(333)    # False
is_power_of_two(0)      # False