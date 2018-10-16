# solution for https://www.hackerrank.com/challenges/binary-search-tree-lowest-common-ancestor/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=trees


def lca(root, v1, v2):
    if root.info < v1 and root.info < v2:
        return lca(root.right, v1, v2)
    elif root.info > v2 and root.info > v1:
        return lca(root.left, v1, v2)
    return root

