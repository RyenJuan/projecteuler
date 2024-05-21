# Project Euler
# Problem 12

import math

answer = 0
number = 1

def find_divisors(n):
    i = 1
    divisors = 0
    while i < math.sqrt(n): # square root because divisors are symmetric past the square root of n
        if(n % i == 0):
            if(n/i == i):
                divisors += 1
            else:
                divisors += 2
        i += 1
        # print(divisors)
    return divisors

def get_triangular_number(x):
    sum = 0
    for i in range(x + 1):
        sum += i
    return sum

x = 100

while(answer < 500):
    answer = find_divisors(get_triangular_number(x))
    x+= 1

print(get_triangular_number(x-1))

# Answer: 76576500
