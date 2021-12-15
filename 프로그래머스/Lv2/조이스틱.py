from copy import deepcopy
from collections import deque
def solution(name):
    dc = [-1,1]
    d = len(name)
    name = list(name)
    answer = 0
    def bfs(now):
        nonlocal answer
        Q = deque([now])
        while Q:
            state = Q.popleft()
            lst,idx,answer = state[0],state[1],state[2]
            answer += min(ord('Z')-ord(name[idx])+1,ord(name[idx]) - ord('A'))
            lst[idx] = 'A'
            if lst == ['A']*d:
                return answer
            for nc in dc:
                next = deepcopy(lst)
                next_idx = idx+nc
                next_answer = answer + 1
                Q.append((next,next_idx,next_answer))
    bfs((name,0,answer))
    return answer
solution("JEROEN")