from itertools import permutations


def lexicographical_permutation(str):
    perm = sorted(''.join(chars) for chars in permutations(str))
    for x in perm:
        yield x


for i, x in enumerate(lexicographical_permutation('0123456789')):
    if i == 1_000_000:
        break
    print(i, x)

