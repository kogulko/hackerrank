# solution for https://www.hackerrank.com/challenges/missing-numbers/problem

def missingNumbers(n, arr, brr):
    counts = [0] * (brr[0] * 2 + 1)
    for i in range(len(brr)):
        if i < n:
            counts[arr[i]] -= 1
        counts[brr[i]] += 1
    return [i for i in range(len(counts)) if counts[i] > 0]
