def dfs(n,cnt):
    global ans
    visit[n] = True
    if cnt >=4:
        ans = 1
        return
    if ans:
        return
    for i in friend[n]:
        if visit[i] ==0:
            dfs(i,cnt+1)
            visit[i]=False
n,m=map(int,input().split())
friend = [[] for _ in range(n)]
for i in range(m):
    r,c = map(int,input().split())
    friend[r].append(c)
    friend[c].append(r)
visit = [0 for _ in range(n)]
cnt = 0
ans = 0
for i in range(n):
    dfs(i,0)
    visit[i] = False
    if ans:
        break
print(1 if ans else 0)
