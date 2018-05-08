# solution for https://www.hackerrank.com/challenges/sherlock-and-array/problem

def solve(a):
    arr_sum = sum(a)
    curr_sum = 0
    for i in range(len(a)):
        if curr_sum == (arr_sum - a[i]) / 2:
            return 'YES'
        curr_sum += a[i]
    return 'NO'


