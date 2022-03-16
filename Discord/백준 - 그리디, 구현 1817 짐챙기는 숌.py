import sys
from collections import deque
input = sys.stdin.readline
n,w = map(int,input().split())
arr = deque(list(map(int,input().split())))
if arr:
    cnt = 1
    tot = 0
    while arr:
        now = arr.popleft()
        if tot+now > w:
           tot = 0
           cnt += 1
        tot += now
        print(cnt,tot,now)
else:
    print(0)