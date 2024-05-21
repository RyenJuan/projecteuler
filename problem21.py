# Project Euler
# Problem 21

def get_divisors(n) :
    all_divisors = []
    i = 1
    while i <= n :
        if (n % i==0) :
             all_divisors.append(i)
        i = i + 1
    all_divisors.pop()
    return all_divisors

def d(n):
    array = get_divisors(n)
    return sum(array)

temp = []
x = 3

ans = 0
while x < 10000:
    p = d(x)
    if d(p) == x and p != x:
        ans += p
        print("( " + str(p) + ", " + str(x) + " )")
    x += 1

print(ans)

