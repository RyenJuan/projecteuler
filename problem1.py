# Project Euler
# Problem 1

triples = [3*i for i in range(1000) if 3*i < 1000]
quintuples = [5*i for i in range(1000) if 5*i < 1000]

combined = sum(list(set(triples + quintuples)))
print(combined)

# Answer: 233168