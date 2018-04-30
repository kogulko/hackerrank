# solution for https://www.hackerrank.com/challenges/marcs-cakewalk/problem

import sys

def marcsCakewalk(calorie):
    calorie.sort(reverse=True)
    sum(map(lambda i: pow(2,i) * calorie[i],range(len(calorie))))
    # Complete this function

if __name__ == "__main__":
    n = int(input().strip())
    calorie = list(map(int, input().strip().split(' ')))
    result = marcsCakewalk(calorie)
    print(result)

