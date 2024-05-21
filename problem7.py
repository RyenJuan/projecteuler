# Project Euler
# Problem 7
from sympy import isprime


def all_primes(limit):
    '''
    Generate a list of primes up to a limit
    :param limit: integer
    :return: list
    '''
    primes = []
    for i in range(1, limit):
        if isprime(i):
            primes.append(i)
    return primes

print(all_primes(150000)[10001])

# Answer: 104759



