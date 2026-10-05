import itertools

def are_equivalent(f, g, n):
    for row in itertools.product((0, 1), repeat=n):
        if f(*row) != g(*row):
            return False
    return True