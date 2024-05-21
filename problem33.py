# Project Euler
# Problem 33

# these are known as anomalous cancellations

prodN = 1
prodD = 1
for i in range(10,100):
    for j in range(10,100):
        if i % 10 == 0 or j % 10 == 0 or i==j: # ignore the trivial cases 30/50 = 3/5
            continue
        a = list(str(i))
        b = list(str(j))
        if any(p in b for p in a):
            c = list(set(a).intersection(b))[0] # find the common element
            q = a.copy()
            r = b.copy()
            q.remove(str(c))
            r.remove(str(c))

            if int(''.join(a)) / int(''.join(b)) == int(q[0]) / int(r[0]) and (int(q[0]) / int(r[0])) < 1:

                prodN *= int(''.join(a))
                prodD *= int(''.join(b))

print(f"{prodN}/{prodD}")

# The answer wants the denominator of the reduced fraction
# Answer: 100