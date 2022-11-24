def is_primes(number):
    if number <= 1:
        return False
    for num in range(2, number):
        if number % num == 0:
            return False
    return True

def get_primes(numbers):
    for number in numbers:
        if is_primes(number):
            yield number

print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))