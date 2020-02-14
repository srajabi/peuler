import functools
import operator


@functools.lru_cache(maxsize=10_000_000)
def collatz(n):
    if n%2 == 0:
        return n//2
    else:
        return 3*n + 1

collatz_lookup = {}

for i in range(1, 1_000_001):
    length = 0
    cur_collatz = i
    while cur_collatz > 1.0:
        pot_length = collatz_lookup.get(cur_collatz, None)

        if pot_length:
            length += pot_length
            break

        cur_collatz = collatz(cur_collatz)
        length += 1

    length += 1

    collatz_lookup[i] = length

print(max(collatz_lookup.items(), key=operator.itemgetter(1)))
