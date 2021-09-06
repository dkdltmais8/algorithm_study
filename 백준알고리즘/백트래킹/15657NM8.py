import itertools
n,m = map(int,input().split())
ans = list(map(int,input().split()))
ans.sort()
res = list(itertools.combinations_with_replacement(ans,m))
for i in res:
    print(*i)