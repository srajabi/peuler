import math
import decimal
import functools


decimal.getcontext().prec = 8000

half_decimal = decimal.Decimal(0.5)


def find_b(t):
    candidate = 1 + 2 * t * (t - 1)
    sqrt_cand = decimal.Decimal(candidate).sqrt()
    if sqrt_cand == sqrt_cand.to_integral_value():
        sqrt_cand = sqrt_cand/2
        b_cand_1 = sqrt_cand + half_decimal
        b_cand_2 = sqrt_cand - half_decimal

        b_1 = None
        b_2 = None
        if b_cand_1 == b_cand_1.to_integral_value():
            b_1 = b_cand_1
        if b_cand_2 == b_cand_2.to_integral_value():
            b_2 = b_cand_2

        return b_1.to_integral_value().as_integer_ratio()[0], b_2.to_integral_value().as_integer_ratio()[0]
    return None, None


def check_valid(b, t):
    return 2 * b * (b - 1) == t * (t - 1)


@functools.lru_cache()
def generate_t(n):
    if n == 0:
        return 1
    elif n == 1:
        return 4
    else:
        return 6 * generate_t(n-1) - generate_t(n-2) - 2


magic_constant = decimal.Decimal(3) + decimal.Decimal(2) * decimal.Decimal(2).sqrt()
def generate_t_nk(n):
    return (n * (magic_constant)).to_integral_value().as_integer_ratio()[0] - 2


totals = []
for n in range(2, 10001):
    totals.append(generate_t(n))

cur_t = 21
totals_nk = [cur_t]
for _ in range(2, 10000):
    cur_t = generate_t_nk(cur_t)
    totals_nk.append(cur_t)


#print(totals)
#print(totals_nk)

print(totals[-1])
print(totals_nk[-1])

#for t in totals:
#    b_1, b_2 = find_b(t)
#    if (b_1 or b_2) and t > 10**12:
        #print(t, b_1, b_2)
#        pass
