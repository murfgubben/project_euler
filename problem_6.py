first_hundred = range(1, 101)
dif = (sum(first_hundred) ** 2) - sum([i ** 2 for i in first_hundred])

print(f'Answer: {dif}')