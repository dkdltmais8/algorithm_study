from itertools import combinations, permutations
n,m = map(int,input().split())
arr = [str(i) for i in range(1, n+1)]
ans = permutations(arr, m)
for i in ans:
    print(' '.join(i))
