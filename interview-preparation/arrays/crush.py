def arrayManipulation(n, queries):
# Instead of storing the actual values in the array,
# you store the difference between the current element
# and the previous element. So you add sum to a[p] showing that a[p]
# is greater than its previous element by sum.
# You subtract sum from a[q+1] to show that a[q+1] is less than a[q]
# by sum (since a[q] was the last element that was added to sum).
# By the end of all this, you have an array that shows the difference
# between every successive element. By adding all the positive differences,
# you get the value of the maximum element
    arr = [0 for i in range(n)]
    x = 0
    max = 0
    for a, b, k in queries:
        arr[a] += k
        if b + 1 <= n:
            arr[b+1] -= sum

    for i in range(1,n+1):
        x += arr[i]
        if max < x:
            max = x
    return max
