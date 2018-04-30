# solution for https://www.hackerrank.com/challenges/countingsort4/problem

def modifiedCountingSort(arr):
    integers = [a[0] for a in arr]
    strings = [a[1] for a in arr]
    count = [[] for i in range(max(integers) + 1)]
    for index, value in enumerate(integers):
        count[value].append(strings[index])
    return [j for i in count for j in i]
