#soltuion for https://www.hackerrank.com/challenges/fraudulent-activity-notifications/problem


import sys
from bisect import bisect_left, insort_left

def activityNotifications(expenditure, d):
    notifications = 0
    sorted_actives = sorted(expenditure[:d])
    half = d // 2

    for p, i in enumerate(expenditure[d:]):
        if (d % 2 != 0 and i >= 2 * sorted_actives[half]) or \
           (d % 2 == 0 and i >= sum(sorted_actives[half - 1:half + 1])):
            notifications += 1
        del sorted_actives[bisect_left(sorted_actives, expenditure[p])]
        insort_left(sorted_actives, i)

    return notifications



if __name__ == "__main__":
    n, d = input().strip().split(' ')
    n, d = [int(n), int(d)]
    expenditure = list(map(int, input().strip().split(' ')))
    result = activityNotifications(expenditure, d)
    print(result)

