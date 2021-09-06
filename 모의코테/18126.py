n = int(input())
lst = [[] for _ in range(n+1)]
visit = [0] * (n+1)
res = 0
for i in range(n-1):
    n1,n2,d = map(int,input().split())
    lst[n1].append([n2,d])
    lst[n2].append([n1,d])
Q = [[1,0]]
while Q:
    g,e = Q.pop()
    visit[g] = 1
    flag = False
    for LEg,LEe in lst[g]:
        if visit[LEg] == 0:
            flag = True
    if flag == True:
        if lst[g]:
            for G,E in lst[g]:
                if visit[G] == 0:
                    Q.append([G, e+E])
    else:
        if e > res:
            res = e
print(res)

