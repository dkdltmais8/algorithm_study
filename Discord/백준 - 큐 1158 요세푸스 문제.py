from collections import deque
import sys
input = sys.stdin.readline
n, k = map(int,input().split())
arr = deque([i for i in range(1,n+1)])
ans = "<"
while arr:
    for i in range(k-1):
        arr.append(arr.popleft())
    ans += str(arr.popleft())
    if len(arr) == 0:
        break
    ans += ', '
ans += '>'
print(ans)