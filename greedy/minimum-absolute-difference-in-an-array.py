# solution for https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array/problem

import sys

def minimumAbsoluteDifference(n, arr):
    arr.sort()
    min = abs(arr[0] - arr[1])
    for i in range(1, len(arr) - 1):
        min = min(min, abs(arr[i] - arr[i+1]))
    return min

    # Complete this function

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    result = minimumAbsoluteDifference(n, arr)
    print(result)

