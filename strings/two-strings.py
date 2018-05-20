# solution for https://www.hackerrank.com/challenges/two-strings/problem
import collections

def twoStrings(s1, s2):
    letters = collections.defaultdict(int)
    for i in s1:
        letters[i] += 1
    for i in s2:
        if letters[i] > 0:
            return 'YES'
    else:
        return 'NO'

