def dfs(arr,tot,idx):
    
n = int(input())
plan = list(map(int,input().split()))
candidate = [list(map(int,input().split())) for _ in range(n)]
print(candidate)
visit = [0]*n
for i in range(n):
    dfs(candidate,0,i)