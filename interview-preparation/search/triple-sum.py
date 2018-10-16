# solution for
# https://www.hackerrank.com/challenges/triple-sum/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=search&h_r=next-challenge&h_v=zen

from collections import defaultdict


def triplets(a, b, c):
    a = sorted(list(set(a)))
    b = sorted(list(set(b)))
    c = sorted(list(set(c)))
    counts_a = count_pairs(a, b)
    counts_c = count_pairs(c, b)

    ans = 0
    for number in counts_a.keys():
        ans += counts_a[number] * counts_c[number]
    return ans


def count_pairs(a, b):
    counts = defaultdict(int)
    i = 0
    index = 0
    count = 0
    while i < len(b):
        if index == len(a):
            break
        elif a[index] <= b[i]:
            count += 1
            index += 1
            counts[b[i]] = count
        else:
            counts[b[i]] = count
            i += 1
    while i < len(b):
        counts[b[i]] = len(a)
        i += 1

    return counts
