# solution for https://www.hackerrank.com/challenges/largest-rectangle/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=stacks-queues&h_r=next-challenge&h_v=zen

def largestRectangle(h):
    max_area = len(h)
    top = 0
    stack = []
    i = 0
    while i < len(h):
        if not stack or h[stack[-1]] <= h[i]:
            stack.append(i)
            i += 1
        else:
            top = stack.pop()
            if not stack:
 #                //if stack is empty means everything till i has to be
 #                //greater or equal to input[top] so get area by
 #                //input[top] * i;
                max_area = max(max_area, h[top] * i)
            else:
 #                //if stack is not empty then everythin from i-1 to input.peek() + 1
 #                //has to be greater or equal to input[top]
 #                //so area = input[top]*(i - stack.peek() - 1);
                max_area = max(max_area, h[top] * (i - stack[-1] - 1))

    while stack:
        top = stack.pop()
        if not stack:
 #            //if stack is empty means everything till i has to be
 #            //greater or equal to input[top] so get area by
 #            //input[top] * i;
            max_area = max(max_area, h[top] * i)
        else:
 #            //if stack is not empty then everything from i-1 to input.peek() + 1
 #            //has to be greater or equal to input[top]
 #            //so area = input[top]*(i - stack.peek() - 1);
            max_area = max(max_area, h[top] * (i - stack[-1] - 1))
    return max_area
