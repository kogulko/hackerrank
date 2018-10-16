# solution for https://www.hackerrank.com/challenges/angry-children/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=greedy-algorithms

def maxMin(k, arr):
    arr = sorted(arr)
    n = len(arr)
    res = float('inf')
    for i in range(k - 1, n):
        res = min(res, arr[i] - arr[i - k + 1])
    return res

