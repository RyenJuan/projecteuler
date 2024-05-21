# Project Euler
# Problem 35

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

def rotation(nums):
    '''
    Generate list of circularly shifted numbers
    :param nums:
    :return:
    '''
    circular_primes = []
    for i in range(len(nums)+1):
        rotated = nums[i:] + nums[:i]
        circular_primes.append(rotated)

    circular_primes.pop() # this for loop includes the original number as a rotation

    return circular_primes

num_primes = all_primes(1000000)
count = 0

for i in num_primes:
    if all(isprime(int(j)) for j in rotation(str(i))):
        count += 1

print(count)

# Answer: 55

