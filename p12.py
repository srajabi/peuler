import math

triangle_nums = [1]

current_num = 1
n_divisors = 0

while n_divisors <= 500:
    current_num += 1
    triangle_nums.append(triangle_nums[current_num-2] + current_num)

    cur_triangle_num = triangle_nums[-1]
    divisors = []
    for i in range(1, math.ceil(math.sqrt(cur_triangle_num))):
        if cur_triangle_num%i == 0:
            divisor_1 = cur_triangle_num//i
            if divisor_1 == i:
                divisors.append(i)
            else:
                divisors.append(i)
                divisors.append(divisor_1)

    n_divisors = len(divisors)

print(triangle_nums)

