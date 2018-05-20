# solution for https://www.hackerrank.com/challenges/insertion-sort/problem
#hint https://www.youtube.com/watch?v=v_wj_mOAlig&t=844s
import sys
import array

def insertionSort(arr, n):
    bits_arr = array.array('i', [0] * 10000001)
    shifts = 0
    for i in range(n):
        shifts += bt_sum(bits_arr, arr[-1 - i] - 1)
        bt_add(bits_arr, arr[-1 - i])
    return shifts

def bt_sum(bits_arr, i):
    result = 0
    while i > 0:
        result += bits_arr[i]
        i -= i & -i
    return result

def bt_add(bits_arr, i):
    while i < 10000001:
        bits_arr[i] += 1
        i += i & -i

    # Complete this function

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        arr = list(map(int, input().strip().split(' ')))
        result = insertionSort(arr, n)
        print(result)

