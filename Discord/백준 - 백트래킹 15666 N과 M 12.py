from itertools import combinations_with_replacement
n,m = map(int,input().split())
arr = sorted(list(map(int,input().split())))
ans = sorted(set(combinations_with_replacement(arr,r=m)))
for i in ans:
    print(*i)
