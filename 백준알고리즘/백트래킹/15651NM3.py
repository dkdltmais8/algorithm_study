from itertools import product

n,m = map(int,input().split())
arr = [str(i) for i in range(1,n+1)]
ans = product(arr,repeat=m)
for i in ans:
    print(' '.join(i))