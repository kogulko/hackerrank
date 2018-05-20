# solution for https://www.hackerrank.com/challenges/maximum-perimeter-triangle/problem
# Logic : Select the longest possible side such that it can form a non-degenerate triangle using the two sides "just smaller" than it.

# It fulfills all other conditions. If no such selection is possible, then no non-degenerate triangle exists.


def maximumPerimeterTriangle(sticks):
    A = sorted(sticks)
    i = len(sticks) - 3
    while i >= 0 and (A[i] + A[i+1] <= A[i+2]) :
        i -= 1

    return [A[i],A[i+1],A[i+2]] if i >= 0 else [-1]


