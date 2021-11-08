import sys
input = sys.stdin.readline
dr = [1,-1,0,0]
dc = [0,0,1,-1]
# def dfs(r,c,cnt):
#     global ans
#     cn = 0
#     for i in range(4):
#         nr = r+dr[i]
#         nc = c+dc[i]
#         if 0<=nr<n and 0<=nc<m and (maps[nr][nc] not in lst):
#             lst.append(maps[nr][nc])
#             dfs(nr,nc,cnt+1)
#             lst.remove(maps[nr][nc])
#         else:
#             cn +=1
#     if cn== 4:
#         ans = max(ans,cnt)
#         return
# n,m = map(int,input().rstrip().split())
# maps = [list(input().rstrip()) for _ in range(n)]
# ans = 1
# lst = [maps[0][0]]
# dfs(0,0,ans)
# print(ans)
dr = [1,-1,0,0]
dc = [0,0,1,-1]
def bfs():
    global ans,maps
    Q = set([(0,0,maps[0][0])])
    while Q:
        r,c,string = Q.pop()
        for i in range(4):
            nr = r+dr[i]
            nc = c+dc[i]
            if 0<=nr<n and 0<=nc<m and maps[nr][nc] not in string:
                Q.add((nr,nc,string+maps[nr][nc]))
                ans = max(ans,len(string)+1)



n,m = map(int,input().rstrip().split())
maps = [list(input().rstrip()) for _ in range(n)]
ans = 1
bfs()
print(ans)
