import sys
input = sys.stdin.readline
n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
ans = [[0]*n for _ in range(n)]
#m이 1일 때는 절댓값으로 출력해주면 된다.
if m == 1:
    for i in arr:
        for j in i:
            print(-j,end=' ')
        print()
else:
    for i in range(n):
        for j in range(n):
            #범위를 조과하지 않는 r,c를 만듦
            r = i+m//2 if i+m//2<n else n-1
            c = j+m//2 if j+m//2<n else n-1
            rr = i-m//2-1 if i-m//2-1>=0 else 0
            cc = j-m//2-1 if j-m//2-1>=0 else 0
            if r>=n or c>=n: continue
            #현재 위치의 누적값 저장
            ans[r][c] = ans[r-1][c] + ans[r][c-1] - ans[r-1][c-1]
            #현재 위치에서 전위치의 누적값을 제거하고 양수로 바꿔줌
            next = -1*((ans[r][c]-ans[r][cc]-ans[rr][c]+ans[rr][cc]) + arr[i][j])
            #그 위치의 값을 dp에 저장
            ans[r][c] += next
    for i in range(n):
        for j in range(n):
            #테두리는 0이기 떄문에 그 이후부터 담겨있는 dp값 출력
            r = i-1 if i-1>=0 else 0
            c = j-1 if j-1>=0 else 0
            next = ans[i][j]-ans[r][j]-ans[i][c]+ans[r][c]
            print(next,end = ' ')
        print()
