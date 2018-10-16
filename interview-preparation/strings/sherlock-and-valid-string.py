# solution for https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings

from collections import Counter

def isValid(s):
    counter = list(Counter(s).values())
    for i in range(1, len(counter)):
        if abs(counter[i] - counter[i - 1]) > 1:
            return 'NO'
    return 'YES'


