# Project Euler
# Problem 14

def collatz(n):
    steps = 1
    while n != 1:
        if n % 2 == 0:
            n = n/2
            steps += 1
        elif n % 2 != 0:
            n = 3*n + 1
            steps += 1

    return steps
x = 100

max_steps = 0
max_steps_val = 0

while x < 1000000:
    p = collatz(x)
    if p > max_steps:
        max_steps = p
        max_steps_val = x
    x += 1
print(max_steps)
print(max_steps_val)

# Answer: 837799




