from itertools import permutations

def possible_permutations(elements):
    result = permutations(elements)

    for perm in result:
        yield list(perm)

[print(n) for n in possible_permutations([1, 2, 3])]