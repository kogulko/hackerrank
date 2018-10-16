# solution for
# https://www.hackerrank.com/challenges/special-palindrome-again/problem


def substrCount(n, s):
    l = []
    cur = None
    count = 0
    ans = 0
    for i in range(n):
        if cur == s[i]:
            count += 1
        else:
            if cur:
                l.append((cur, count))
            cur = s[i]
            count = 1
    l.append((cur, count))

    for letter, count in l:
        ans += (count * (count + 1)) // 2

    for i in range(1, len(l) - 1):
        if l[i - 1][0] == l[i+1][0] and l[i][1] == 1:
            ans += min(l[i - 1][1], l[i+1][1])

    return ans
