from collections import deque
def solution(begin, target, words):
    def bfs(now):
        Q = deque()
        Q.append((now,0))
        while Q:
            now,idx = Q.popleft()
            if now == target:
                return idx
            for i in range(n):
                cnt = 0
                for j in range(len(words[i])):
                    if now[j] != words[i][j]:
                        cnt +=1
                if cnt == 1 and visit[i] ==0:
                    Q.append((words[i],idx+1))
                    visit[i] = 1



    answer = 0
    n = len(words)
    visit = [0]*n
    if target not in words:
        return 0
    answer = bfs(begin)
    # print(answer)
    return answer
solution("hit"	,"cog"	,["hot", "dot", "dog", "lot", "log", "cog"])
solution("hit"	,"cog"	,["hot", "dot", "dog", "lot", "log"])