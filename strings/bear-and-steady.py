# solution for https://www.hackerrank.com/challenges/bear-and-steady-gene/forum
from collections import defaultdict

def validity_check(dict, limit):
    return all(x <= limit for x in dict.values)


def steadyGene(gene, n):
    tail = 0
    out = 99999999
    limit = n // 4
    dict = defaultdict(int)
    for i in range(n - 1, -1, -1):
        dict[gene[i]] += 1
        if not validity_check(dict, limit):
            tail = i + 1
            dict[gene[i]] -= 1
            break

    head = -1
    while  head < n - 1 and tail < n and head < tail:
        while not validity_check(dict, limit) and tail < n:
            dict[gene[tail]] -= 1
            tail += 1
        if tail < n or not validity_check(dict, limit):
            break
        sub_len = max(0, tail - head - 1)
        if sub_len < out:
            out = sub_len
        dict[gene[head + 1]] += 1
        head += 1
    return out
