# solution for
# https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem
import collections

# The idea is to create a map. We use character frequencies as keys and corresponding counts as values. We can solve this problem by iterating over all substrings and counting frequencies of characters in every substring. We can update frequencies of characters while looping over substrings i.e. there won’t be an extra loop for counting frequency of characters.
# In below code, a map of key ‘vector type’ and value ‘int type’ is taken
# for storing occurrence of ‘frequency array of length 26’ of substring
# characters. Once occurrence ‘o’ of each frequency array is stored, total
# anagrams will be the sum of o*(o-1)/2 for all different frequency arrays
# because if a particular substring has ‘o’ anagrams in string total
# o*(o-1)/2 anagram pairs can be formed.


def sherlockAndAnagrams(s):
    N = len(s)
    to_num = lambda x: ord(x) - 97
    mp = collections.defaultdict(int)
    for i in range(N):
        freq = [0] * 26
        for j in range(i, N):
            freq[to_num(s[j])] += 1
            mp[tuple(freq)] += 1
    return mp
