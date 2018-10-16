# solution for https://www.hackerrank.com/challenges/pairs/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=search

from collections import defaultdict

def pairs(k, arr):
    ans = 0
    counts = defaultdict(int)
    for i in arr:
        counts[i] += 1
    keys = list(counts.keys())
    for number in keys:
        ans += min(counts[number], counts[number + k])
    return ans
