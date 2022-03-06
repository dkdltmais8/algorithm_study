import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n, k = map(int,input().split())
    arr = list(map(int,input().split()))
    arr.sort()
    ans = 0
    tot = float('inf')
    for i in range(len(arr)):
        idx1,idx2 = i+1,len(arr)-1
        while idx1<=idx2:
            m = (idx1+idx2)//2
            now = arr[i]+arr[m]
            if now>k:
                idx2 = m-1
            else:
                idx1 = m+1
            if (abs(k-now))<tot:
                ans = 1
                tot = abs(k-now)
            elif (abs(k-now)) == tot:
                ans += 1
    print(ans)