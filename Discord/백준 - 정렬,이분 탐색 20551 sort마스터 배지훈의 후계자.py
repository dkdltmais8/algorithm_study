import sys
input = sys.stdin.readline
n,m = map(int,input().split())
Q = list()
for i in range(n):
    s = int(input())
    Q.append(s)
Q = sorted(Q)
dic = dict()
for idx,v in enumerate(Q):
    if v in dic:
        continue
    dic[v] = idx
for i in range(m):
    s = int(input())
    print(dic[s] if s in dic else -1)