# solution for https://www.hackerrank.com/challenges/lilys-homework/problem
# hint = https://www.geeksforgeeks.org/minimum-number-swaps-required-sort-array/


import sys

def lilysHomework(arr):
    return min(swaps_number(arr), swaps_number(arr, True))

def swaps_number(arr, reverse=False):
    pairs = sorted([[arr[i], i] for i in range(len(arr))], key=lambda x: x[0], reverse=reverse)
    visited = [False] * len(arr)
    res = 0
    for i in range(len(arr)):
    #     // already swapped and corrected or
    #     // already present at correct pos
        if visited[i] or pairs[i][1] == i:
            continue
    #     // find out the number of  node in
    #     // this cycle and add in ans
        cycle_size = 0
        j = i
        while not visited[j]:
            visited[j] = True
            #move to next node
            j = pairs[j][1]
            cycle_size += 1

        #Update answer by adding current cycle
        res += (cycle_size - 1)
    return res

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    result = lilysHomework(arr)
    print(result)
