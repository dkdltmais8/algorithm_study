import itertools
n,m = map(int,input().split())
ans = list(map(int,input().split()))
ans.sort()
res = list(itertools.combinations(ans,m))
for i in res:
    print(*i)