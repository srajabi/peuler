import math


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


sum_divisors_lookup = {}
for i in range(1, 10001):
    print(i, find_divisors(i))
    divisors_sum = sum(find_divisors(i))
    sum_divisors_lookup[i] = divisors_sum


amicable_numbers = []
for k, v in sum_divisors_lookup.items():
    amicable_candidate = sum_divisors_lookup.get(v, None)
    if amicable_candidate == k and k != v:
        amicable_numbers.append(amicable_candidate)
        #amicable_numbers.append(k)

print(sum_divisors_lookup)
print(amicable_numbers)
print(sum(amicable_numbers))


