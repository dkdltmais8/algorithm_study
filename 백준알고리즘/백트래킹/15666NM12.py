import itertools
n,m = map(int,input().split())
arr = sorted(list(map(int,input().split())))
ans = list(itertools.combinations_with_replacement(arr,m))
res = []
for i in ans:
    if i not in res:
        res.append(i)
for i in res:
    print(*i)

