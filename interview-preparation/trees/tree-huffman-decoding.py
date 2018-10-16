# solution for https://www.hackerrank.com/challenges/tree-huffman-decoding/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=trees&h_r=next-challenge&h_v=zen

def decodeHuff(root, s):
    ans = []
    current = root
    for c in s:
        if c == '0':
            current = current.left
        elif c == '1':
            current = current.right
        if not(current.left or current.right):
            ans.append(current.data)
            current = root
    return print(''.join(ans))

