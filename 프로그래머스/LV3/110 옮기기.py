from collections import deque
def solution(s):
    answer = []
    for i in s:
        stack = []
        cnt = 0
        for j in i:
            if j == '0':
                if stack[-2:] == ['1','1']:
                    cnt += 1
                    stack.pop()
                    stack.pop()
                else:
                    stack.append(j)
            else:
                stack.append(j)
        if cnt == 0:
            answer.append(i)
        else:
            Q = deque()
            while stack:
                if stack[-1] == '1':
                    Q.append(stack.pop())
                else:
                    break
            while cnt>0:
                Q.appendleft('0')
                Q.appendleft('1')
                Q.appendleft('1')
                cnt -= 1
            while stack:
                Q.appendleft(stack.pop())
            answer.append(''.join(Q))
    return answer
solution(["1110","100111100","0111111010"])