#If reversed string is equal to regular it is a palindrome
def is_palindrome(n):
    str_n = str(n)
    if str_n[::-1] == str_n:
        return True
    
largest_palindrome = 0

for i in range(100, 1000):
    for j in range(100, 1000):
        product = i * j
        if is_palindrome(product) and product > largest_palindrome:
            largest_palindrome = product

print(f'Answer: {largest_palindrome}')