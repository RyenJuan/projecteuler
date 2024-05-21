# Project Euler
# Problem 3
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

n = 600851475143

divisors = all_primes(10000)

prime_factors = []

for i in divisors:
    if n % i == 0:
        n = n/i
        prime_factors.append(i)

print(max(prime_factors))

# Answer: 6857
