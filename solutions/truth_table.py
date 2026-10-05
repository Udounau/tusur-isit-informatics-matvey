import itertools

def truth_table(n):
    return list(itertools.product((0, 1), repeat=n))