# solution for https://www.hackerrank.com/challenges/palindrome-index/problem

def palindromeIndex(s):
    n = len(s)
    start = 0
    end = n - 1
    while start < end:
        if s[start] != s[end]:
            if s[start + 1] == s[end] and s[start + 2] == s[end -1]:
                return start
            else:
                return end
        start += 1
        end -= 1
    return -1
