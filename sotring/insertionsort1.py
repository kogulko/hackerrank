# solution for https://www.hackerrank.com/challenges/insertionsort1/problem
import sys


def insertionSort1(n, arr):
    value = arr[-1]
    for i in range(0, len(arr) - 1):
        if value >= arr[-1 - i - 1]:
            arr[-1 - i] = value
            output(arr)
            break
        else:
            arr[-1 - i] = arr[-1 - i - 1]
            output(arr)
    else:
        arr[1] = arr[0]
        arr[0] = value
        output(arr)

def output(arr):
    print(' '.join([str(i) for i in arr]))

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    insertionSort1(n, arr)
