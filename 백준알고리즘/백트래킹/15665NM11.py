import itertools
n,m = map(int,input().split())
arr = list(set(list(map(int,input().split()))))
ans = sorted(list(itertools.product(arr,repeat=m)))
for i in ans:
    print(*i)
