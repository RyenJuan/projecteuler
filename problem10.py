# Project Euler
# Problem 10
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

print(sum(all_primes(2000000)))

# Answer: 142913828922