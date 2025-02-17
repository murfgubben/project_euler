previous = [1, 2]

fib = 2
even_sum = 0
while fib < 4000000:
    if fib % 2 == 0:
        even_sum += fib
    previous = [fib, previous[0]]
    fib = sum(previous)

print(even_sum)
