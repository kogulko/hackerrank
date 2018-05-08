# solution for https://www.hackerrank.com/challenges/making-anagrams/problem
import collections

def makingAnagrams(s1, s2):
    l1 = len(s1)
    l2 = len(s2)
    n = max(l1, l2)
    letters = collections.defaultdict(int)
    for i in range(n):
        if i < l1:
            letters[s1[i]] += 1
        if i < l2:
            letters[s2[i]] -= 1
    return  sum(map(abs,letters.values()))

    # Complete this function
