from itertools import combinations

n,m = map(int,input().split())
arr = [str(i) for i in range(1,n+1)]
ans = combinations(arr,m)
for i in ans:
    print(' '.join(i))