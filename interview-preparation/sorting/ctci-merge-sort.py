# solution for
# https://www.hackerrank.com/challenges/ctci-merge-sort/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting


def countInversions(arr):
    temp = [0] * len(arr)
    return mergesort(arr, temp, 0, len(arr) - 1)


def mergesort(arr, temp, left_start, right_end):
    if left_start >= right_end:
        return 0
    inversions = 0
    middle = (left_start + right_end) // 2
    inversions += mergesort(arr, temp, left_start, middle)
    inversions += mergesort(arr, temp, middle + 1, right_end)
    inversions += merge_halves(arr, temp, left_start, middle + 1, right_end)
    return inversions


def merge_halves(arr, temp,left_start, middle, right_end):
    inversions = 0
    i = left_start
    j = middle
    index = i
    while i <= middle - 1 and j <= right_end:
        if arr[i] <= arr[j]:
            temp[index] = arr[i]
            i += 1
        else:
            temp[index] = arr[j]
            j += 1
            inversions += (middle - i)
        index += 1

    while i <= middle - 1:
        temp[index] = arr[i]
        i += 1
        index += 1

    while j <= right_end:
        temp[index] = arr[j]
        j += 1
        index += 1

    for p in range(left_start, right_end +1):
        arr[p] = temp[p]

    return inversions

