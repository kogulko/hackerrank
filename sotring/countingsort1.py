# solution for https://www.hackerrank.com/challenges/countingsort1/problem
def countingSort(arr):
    count = [0] * (1 + max(arr))
    for i in arr:
        count[i] += 1
    return [j for i in range(0, len(count)) for j in [i] * count[i]]


if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    result = countingSort(arr)
    print (" ".join(map(str, result)))
