# Project Euler
# Problem 30

def make_list(n):
    lst = list(map(int, str(n)))
    return lst


def sum_of_fifths(x):
    sum = 0
    p = make_list(x)
    for i in p:
        sum += (i**5)
    if sum == x:
        return True

ans = 0

for i in range(2,800000): # not including 1
    if sum_of_fifths(i):
        ans += i

print(ans)

# Answer: 443839

