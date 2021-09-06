import itertools
n,m = map(int,input().split())
ans = [str(i) for i in range(1,n+1)]
res = itertools.combinations_with_replacement(ans,m)
for i in res:
    print(' '.join(i))