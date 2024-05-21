# Project Euler
# Problem 25

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

for i in range(10000):
    if len(str(fibonacci(i))) > 999:
        print(f"i: {i}  | {len(str(fibonacci(i)))}")
        break

# Answer: 4782