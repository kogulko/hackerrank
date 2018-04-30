# solution for https://www.hackerrank.com/challenges/icecream-parlor/problem

import sys

def icecreamParlor(m, arr):
    arr = quickSort(m, arr)
    for i in range(0,len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == m:
                return [a[i], a[j]]
    # Complete this function

def quickSort(m, a):
    if len(a) < 2:
        return a
    pivot = a.pop(0)
    return quickSort(m, list(filter(lambda c: c < pivot and c < m, a))) + \
            [pivot] + \
           quickSort(m, list(filter(lambda c: c > pivot and c < m, a)))


if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        m = int(input().strip())
        n = int(input().strip())
        arr = list(map(int, input().strip().split(' ')))
        result = icecreamParlor(m, arr)
        print (" ".join(map(str, result)))

