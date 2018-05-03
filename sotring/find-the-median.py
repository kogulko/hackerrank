# solution for https://www.hackerrank.com/challenges/find-the-median/problem
# en.wikipedia.org/wiki/Selection_algorithm


import sys
import random

def findMedian(arr, k):
    pivot = arr.pop(random.randrange(len(arr)))
    less = [i for i in arr if i <= pivot]
    more = [i for i in arr if i > pivot]
    if len(less) == k:
        return pivot
    elif len(less) > k:
        return findMedian(less, k)
    else:
        return findMedian(more, k - len(less) - 1)


if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    result = findMedian(arr, n // 2)
    print(result)

