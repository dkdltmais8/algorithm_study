from itertools import product
n,m = map(int,input().split())
arr = list(set((map(int,input().split()))))
arr.sort()
for i in product(arr,repeat=m):
    print(*i)