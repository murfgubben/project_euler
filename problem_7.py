def is_prime(n):
    return not (n < 2 or any(n % x == 0 for x in range(2, int(n ** 0.5) + 1)))

primes = [2]
i = 3
while len(primes) < 10001:
    if is_prime(i):
        primes.append(i)
    i += 2

print(primes[-1])