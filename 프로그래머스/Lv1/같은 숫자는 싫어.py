def solution(arr):
    stack = []
    for i in arr:
        if len(stack)>0:
            if stack[-1] == i:
                continue
        stack.append(i)
    return stack
solution([1,1,3,3,0,1,1])