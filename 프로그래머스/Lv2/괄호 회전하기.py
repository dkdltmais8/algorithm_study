from collections import deque
def solution(s):
    def check(lst):
        s = []
        for i in lst:
            if not s:
                s.append(i)
                continue
            if i ==')':
                if s[-1] == '(':
                    s.pop()
                else:
                    return False
            elif i=='}':
                if s[-1] =='{':
                    s.pop()
                else:
                    return False
            elif i==']':
                if s[-1] == '[':
                    s.pop()
                else:
                    return False
            else:
                s.append(i)
        if not s:
            return True

    answer = 0
    lst = deque(s)
    for i in range(len(lst)):
        if i == 0:
            if check(lst):
                answer += 1
            continue
        a = lst.popleft()
        lst.append(a)
        if check(lst):
            answer += 1
    # print(answer)
    return answer
solution("[](){}")