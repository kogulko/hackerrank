
import sys


def insertionSort2(n, arr):
    shifts = 0
    for i in range(1, n):
        key = arr[i]
        while i > 0 and arr[i - 1] > key:
            arr[i] = arr[i - 1]
            shifts +=1
            i -= 1
        arr[i] = key
        output(arr)
    print(shifts)

def output(arr):
    print(' '.join(map(str, arr)))

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    insertionSort2(n, arr)
