# Project Euler
# Problem 9
import math

N = 500
triples = []

# this algorithm sweeps values of y and z given an x to find pythagorean triples.
for x in range(1,N):
    y = x+1
    z = y+1
    while z <= N:
        if z ** 2 == x ** 2 + y ** 2:
            triples.append([x, y, z])
        while z**2 < x**2 + y**2:
            z += 1
            if z**2 == x**2 + y**2:
                triples.append([x,y,z])
        y += 1

for i in triples:
    if sum(i) == 1000:
        print(math.prod(i))

# Answer: 31875000




