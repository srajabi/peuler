

fib_nums = [1, 1]
threshold = 10**999
print(threshold)
cur_fib = 1
while cur_fib < threshold:
    cur_fib = fib_nums[-1] + fib_nums[-2]
    fib_nums.append(cur_fib)

print(len(str(cur_fib)))
print(len(fib_nums), cur_fib, fib_nums[-1], fib_nums[-2])