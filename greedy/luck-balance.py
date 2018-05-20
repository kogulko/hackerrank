# solution for https://www.hackerrank.com/challenges/luck-balance/problem

def luckBalance(n, k, contests):
    important = sorted(filter(lambda x: x[1] == 1, contests), key=lambda x: x[0])
    looses = len(important) - k if len(important) >= k else 0
    luck = sum(i[0] for i in filter(lambda x: x[1] == 0, contests))
    return luck + sum(i[0] for i in important[looses:]) - sum(i[0] for i in important[:looses])

