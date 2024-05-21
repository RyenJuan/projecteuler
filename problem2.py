# Project Euler
# Problem 2

def fibonacci(n):
    '''
    Generates the nth fibonacci number
    :param n: Integer
    :return: Integer
    '''
    a = 1
    b = 2
    current = 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    else:
        i=0
        while i < n-3:
            current = a+b
            a=b
            b=current
            i += 1
        return current

results = []
for i in range(4000):
    print(i)
    if fibonacci(i) < 4000000:
        if fibonacci(i) % 2 == 0:
            results.append(fibonacci(i))

print(sum(results))

# Answer: 4613732

