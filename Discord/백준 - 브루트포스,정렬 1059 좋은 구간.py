import sys
input = sys.stdin.readline

L = int(input())
arr = list(map(int,input().split()))
n = int(input())
arr.sort()
ans = 0
if arr[0]>n:
    for r in range(1, n + 1):
        for c in range(arr[0]-1, n - 1, -1):
            if r == c:
                continue
            ans += 1
    print(ans)
else:
    for i in range(L):
        if arr[i] == n:
            print(0)
            break
        if arr[i]>n:
            s = arr[i-1]+1
            e = arr[i] - 1
            if n == s or n == e:
                ans = e - s
                print(ans)
                break
            else:
                for r in range(s, n + 1):
                    for c in range(e, n - 1, -1):
                        if r == c:
                            continue
                        ans += 1
                print(ans)
                break