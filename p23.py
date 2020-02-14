import math
from bisect import bisect_left


def find_divisors(n):
    sqrt_n = math.sqrt(n)

    divisors = []
    for i in range(1, math.ceil(sqrt_n)):
        if n%i == 0:
            divisor_1 = n//i
            if divisor_1 == i:
                divisors.append(i)
            else:
                divisors.append(i)

                if divisor_1 != n:
                    divisors.append(divisor_1)

    if sqrt_n%1 == 0:
        divisors.append(int(sqrt_n))

    return divisors


upper_limit = 28123
abundant_numbers = set()
abundant_numbers_list = []

for i in range(1, upper_limit + 1):
    divisors = find_divisors(i)

    if i < sum(divisors):
        abundant_numbers.add(i)
        abundant_numbers_list.append(i)

print(abundant_numbers)
print(abundant_numbers_list)


def check_if_not_sum(i):
    closest = bisect_left(abundant_numbers_list, i)
    for j in range(0, closest+1):
        addend = i - abundant_numbers_list[j]
        if addend < 0:
            continue
        elif addend in abundant_numbers:
            #print(addend, i, abundant_numbers_list[i])
            return False

    return True


results = []
for i in range(1, upper_limit):
    if check_if_not_sum(i):
        results.append(i)

print(results)
print(sum(results))


