# solution for https://www.hackerrank.com/challenges/closest-numbers/problem

def closestNumbers(arr):
    arr.sort()
    min_diff = abs(arr[1] - arr[0])
    res = [arr[0], arr[1]]
    for i in range(1, len(arr) - 1):
        if min_diff > abs(arr[i + 1] - arr[i]):
            min_diff = abs(arr[i + 1] - arr[i])
            res = [arr[i], arr[i + 1]]
        elif min_diff == abs(arr[i + 1] - arr[i]):
            res.extend([arr[i], arr[i + 1]])
    return res
    # Complete this function

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    result = closestNumbers(arr)
    print (" ".join(map(str, result)))

