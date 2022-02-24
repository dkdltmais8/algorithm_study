from itertools import combinations
import sys
input = sys.stdin.readline
n,m = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
ans = list(combinations(arr,m))
ans = sorted(list(set(ans)))
for i in ans:
    print(*i)
