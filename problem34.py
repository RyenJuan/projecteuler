# Project Euler
# Problem 34

import math

def sum(x):
    p = 0
    o = list(map(int, str(x)))
    for i in o:
        p += math.factorial(i)
    if p == x:
        return True

ans = 0

for i in range(3, 100000):
    if sum(i):
        ans += i

print(ans)

# Answer: 40730






