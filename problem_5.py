range_cap = 20
n = range_cap

while True:
    n += range_cap
    evenly_divisible = True
    for i in range(1, range_cap + 1):
        if n % i != 0:
            evenly_divisible = False
            break
    if evenly_divisible:
        break

print(f'Answer: {n}')
