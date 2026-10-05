import random

def birthday_probability(people):
    if people > 365:
        return 1.0
    p_no_match = 1.0
    for i in range(people):
        p_no_match *= (365 - i) / 365
    return 1.0 - p_no_match

def simulate_birthday(people, trials):
    matches = 0
    for _ in range(trials):
        birthdays = [random.randint(1, 365) for _ in range(people)]
        if len(birthdays) != len(set(birthdays)):
            matches += 1
    return matches / trials