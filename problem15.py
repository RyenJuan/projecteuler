# Project Euler
# Problem 15

# recognize that the number of paths through an nxn grid forms pascals triangle
# the center of every odd row is the number of paths
# https://mathschallenge.net/full/random_routes

from math import factorial
import math


# generate pascals triangle
n = 41
for i in range(0, n, 2):
    for j in range(i+1):
        # nCr = n!/((n-r)!*r!)
        if math.floor((i+1)/2)+1 == j:
            print(f"Paths: {factorial(i)//(factorial(j)*factorial(i-j))}")

    # for new line
    print()

# Answer: 131282408400