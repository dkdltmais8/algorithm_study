def check(lst):
    cnt = 0
    for i in range(n-1):
        if lst[i] == 'A':
            for j in range(i+1,n):
                if lst[j] == 'B':
                    cnt += 1
    return cnt
import sys
input = sys.stdin.readline
n,k = map(int,input().split())
ans = ['B']*n
for i in range(n):
    ans[i] = 'A'
    if check(ans) == k:
        break
    elif check(ans)>k:
        ans[i] = 'B'
    else:
        continue
answer = ''.join(ans)
if answer == 'B'* n or answer == 'A'*n:
    if k == 0:
        print(answer)
    else:
        print(-1)
else:
    print(answer)