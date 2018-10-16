# solution for https://www.hackerrank.com/challenges/ctci-is-binary-search-tree/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=trees

def checkBST(root):
    # prev is a global variable
    global prev
    prev = None
    return isbst_rec(root)


# Helper function to test if binary
# tree is BST
# Traverse the tree in inorder fashion
# and keep track of previous node
# return true if tree is Binary
# search tree otherwise false
def isbst_rec(root):

    # prev is a global variable
    global prev

    # if tree is empty return true
    if root is None:
        return True

    if isbst_rec(root.left) is False:
        return False

    # if previous node'data is found
    # greater than the current node's
    # data return fals
    if prev is not None and prev.data >= root.data:
        return False

    # store the current node in prev
    prev = root
    return isbst_rec(root.right)
