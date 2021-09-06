from collections import deque

n = int(input())
node = [[] for _ in range(n)]
parent = list(map(int,input().split()))
d = int(input())
def dfs(root):
    global cnt
    if len(node[root]) == 0:
        cnt += 1
    else:
        for i in node[root]:
            dfs(i)
for i in range(n):
    if parent[i] == -1:
        root = i
    else:
        node[parent[i]].append(i)
# print(node)

for i in range(n):
    if d in node[i]:
        node[i].remove(d)
# print(node)
cnt = 0
if d != root:
    dfs(root)
print(cnt)