# Project Euler
# Problem 4

def is_palindrome(n):
    '''
    Checks if integer n is a palindrome
    :param n: integer
    :return: Boolean
    '''
    n = str(n)
    if n == n[::-1]:    # 'string'[::-1] will reverse a string to "gnirts"
        return True
    return False

results = []
for i in range(100,1000):
    for j in range(100,1000):
        if is_palindrome(i*j):
            results.append(i*j)



print(max(results))

# Answer: 906609