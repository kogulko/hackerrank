# solution for https://www.hackerrank.com/challenges/anagram/problem
import collections

def anagram(s):
    slen = len(s)
    if slen % 2 == 1:
        return -1
    return makingAnagrams(s[slen // 2:], s[:slen // 2], slen // 2)

def makingAnagrams(s1, s2, n):
    letters = collections.defaultdict(int)
    for i in range(n):
        letters[s1[i]] += 1
        letters[s2[i]] -= 1
    return  sum(filter(lambda x: x > 0,letters.values()))
