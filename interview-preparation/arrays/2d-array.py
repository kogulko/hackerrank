import math


def hourglassSum(arr):
    maxSum = -math.inf
    for i in range(0, len(arr) - 2):
        for j in range(0, len(arr[i]) - 2):
            sum = hourglass(arr, i, j)
            if maxSum < sum:
                maxSum = sum
    return maxSum


def hourglass(arr, i, j):
    return sum(arr[i][j:(j+3)]) + arr[i+1][j+1] + sum(arr[i+2][j:(j+3)])
