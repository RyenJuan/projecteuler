# Project Euler
# Problem 29

import math

def log(a):
    return math.log10(a)

distinct = []
for i in range(2,101):
    for j in range(2,101):
        x = i**j
        if x in distinct:
            continue
        else:
            distinct.append(x)
print(len(distinct))

# Answer: 9183