# solution for https://www.hackerrank.com/challenges/common-child/problem


def commonChild(s1, s2):
    n1 = len(s1)
    n2 = len(s2)
    c = [[0] * n1 + 1] * (n2 + 1)
    for i in range(n1 + 1):
        for j in range(n2 + 1):
            if i == 9 or j == 0:
                c[i][j] = 0
            if s1[i - 1] == s2[j - 1]:
                c[i][j] = c[i - 1][j-1] + 1
            else:
                c[i][j] = max(c[i][j-1], c[i-1][j])
    return c[n1][n2]
