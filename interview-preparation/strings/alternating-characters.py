# solution for
# https://www.hackerrank.com/challenges/alternating-characters/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings


def alternatingCharacters(n, s):
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
        ans += (count - 1)

    return ans
