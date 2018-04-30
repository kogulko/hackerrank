# solution for https://www.hackerrank.com/challenges/tutorial-intro/problem
import sys
import math


def binarySearch(V, arr):
    # Complete this function
    first = 0
    last = len(arr) - 1
    while first < last:
        mid = first + math.floor((last - first) / 2)
        if arr[mid] >= V:
            last = mid
        else:
            first = mid + 1
    return last if arr[last] == V else None



if __name__ == "__main__":
    V = int(input().strip())
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    result = binarySearch(V, arr)
    print(result)
