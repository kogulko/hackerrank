import sys

def quickSort(a):
    if len(a) < 2:
        return a
    pivot = a.pop(0)
    return list(filter(lambda c: c < pivot, a)) + \
            [pivot] + \
           list(filter(lambda c: c > pivot, a))

    # Complete this function

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    result = quickSort(arr)
    print (" ".join(map(str, result)))

