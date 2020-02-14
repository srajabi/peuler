import functools


@functools.lru_cache(maxsize=100)
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)


big_factorial = factorial(100)
str_factorial = str(big_factorial)

sum = 0
for c in str_factorial:
    sum += int(c)

print(sum)