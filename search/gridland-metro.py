#solution for https://www.hackerrank.com/challenges/gridland-metro/problem

import sys
from collections import defaultdict

def gridlandMetro(n, m, k, track):
    count = 0
    trains = defaultdict(list)
    for row, start, end in track:
        if not trains[row]:
            trains[row].append([start,end])
        else:
            for interval in trains[row]:
                if interval[0] > start and interval[0] <= end < interval[1]:
                    interval[0] = start
                    break
                elif interval[1] < end and interval[0] < start <= interval[1]:
                    interval[1] = end
                    break
                elif interval[0] >= start and interval[1] <= end:
                    interval[0] = start
                    interval[1] = end
                    break
                elif interval[0] <= start and interval[1] >= end: break
            else:
                trains[row].append([start,end])
    return n * m - sum([j - i + 1 for i,j in (j for i in trains.values() for j in i)])


if __name__ == "__main__":
    n, m, k = input().strip().split(' ')
    n, m, k = [int(n), int(m), int(k)]
    track = []
    for track_i in range(k):
       track_t = [int(track_temp) for track_temp in input().strip().split(' ')]
       track.append(track_t)
    result = gridlandMetro(n, m, k, track)
    print(result)

