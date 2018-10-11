# solution for https://www.hackerrank.com/challenges/ctci-ransom-note/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps

from collections import Counter

def checkMagazine(magazine, note):
    print('No') if Counter(note) - Counter(magazine) else print('Yes')

