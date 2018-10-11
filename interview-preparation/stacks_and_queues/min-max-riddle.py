# solution for https://www.hackerrank.com/challenges/min-max-riddle/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=stacks-queues


def riddle(arr):
    ans = [0 for i in range(len(arr))]
    n = len(arr)
    heights_backward = [0 for i in range(len(arr))]
    heights_forward = [0 for i in range(len(arr))]
    haights = [0 for i in range(len(arr))]
    # Create a stack and push index of fist element to it
    stack_backward = []
    stack_backward.append(0)
    stack_forward = []
    stack_forward.append(0)

    # Span value of first element is always 1
    heights_backward[0] = 1
    heights_forward[0] = 1

    # Calculate span values for rest of the elements
    for i in range(1, n):

        # Pop elements from stack whlie stack is not
        # empty and top of stack is smaller than price[i]
        while( len(stack_backward) > 0 and arr[stack_backward[-1]] >= arr[i]):
            stack_backward.pop()

        while( len(stack_forward) > 0 and arr[-1 - stack_forward[-1]] >= arr[-1 - i]):
            stack_forward.pop()
        # If stack becomes empty, then price[i] is greater
        # than all elements on left of it, i.e. price[0],
        # price[1], ..price[i-1]. Else the price[i]  is
        # greater than elements after top of stack
        heights_backward[i] = i+1 if len(stack_backward) <= 0 else (i - stack_backward[-1])
        heights_forward[i]= i+1 if len(stack_forward) <= 0 else (i - stack_forward[-1])

        # Push this element to stack
        stack_backward.append(i)
        stack_forward.append(i)
    heights_forward = heights_forward[::-1]
    heights = [heights_forward[i] + heights_backward[i] -1 for i in range(len(arr))]
    for i in range(len(heights)):
        ans[heights[i] - 1] = max(ans[heights[i] - 1], arr[i])
    for i in range(1,len(ans)):
        if ans[-1 - i] < ans[-1 - i + 1]:
            ans[-1 - i] = ans[-1 - i + 1]

    return ans
