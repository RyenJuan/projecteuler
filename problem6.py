# Project Euler
# Problem 6

sum_squares = sum([i**2 for i in range(1,101)])
square_sums = sum([i for i in range(1,101)])**2

print(square_sums - sum_squares)

# Answer: 25164150