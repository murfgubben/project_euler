import math

def is_prime(n):
    return not (n < 2 or any(n % x == 0 for x in range(2, int(n ** 0.5) + 1)))

n = 600851475143
prime_factors = []

for i in range(2, n + 1):
    if n % i == 0:
        if is_prime(i):
            prime_factors.append(i)
            if math.prod(prime_factors) == n:
                break

print(f'Answer: {prime_factors[-1]}')