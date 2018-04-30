# solution for https://www.hackerrank.com/challenges/caesar-cipher-1/problem
def caesarCipher(s, k):
    res = []
    for char in s:
        if char.islower():
            res.append(rotate(char, 96))
        elif char.isupper():
            res.append(rotate(char, 64))
        else:
            res.append(char)
    return ''.join(res)

def rotate(char, offset):
    chr((ord(char) - offset + k % 26) % (26 + (1 if (ord(char) - offset + k) % 26 == 0 else 0)) + offset)
