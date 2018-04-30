# solution for https://www.hackerrank.com/challenges/the-power-sum/forum

# HINT https://www.youtube.com/watch?v=tGKS6R7QS1A

#                  (10,2,1)                   ->1^2
#                 /        \
#                /          \
#          (10,2,2)        (9,2,2)            ->2^2
#          /     \         /     \
#         /       \       /       \
#     (10,2,3) (6,2,3)  (9,2,3) (5,2,3)       ->3^2
#     /     \      |       |       |
#    /       \     0       1       0
# (10,2,4) (1,2,4)                            ->4^2
#     |       |
#     0       0

import sys


def powerSum(X, N, num):
    if pow(num, N) < X:
        return powerSum(X, N, num+1) + powerSum(X-pow(num, N), N, num+1)
    elif pow(num, N) == X:
        return 1
    else:
        return 0


if __name__ == "__main__":
    X = int(input().strip())
    N = int(input().strip())
    result = powerSum(X, N, 1)
    print(result)
