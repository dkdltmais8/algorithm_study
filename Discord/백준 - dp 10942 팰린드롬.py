import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int,input().split()))
dp = [[0]*(N) for _ in range(N)]
for i in range(N):
    for j in range(N-i):
        k = i+j
        # 시작과 끝이 같으면 무조건 가능
        if j == k:
            dp[j][k] = 1
        # 다른 인덱스가 값이 같을 때
        elif arr[j] == arr[k]:
            #길이가 2이면 무조건 가능이고
            if j+1 == k: dp[j][k] = 1
            #그게 아니라면 시작+1, 끝-1 이 가능이면 이것도 가능
            elif dp[j+1][k-1] == 1: dp[j][k] = 1

for i in range(int(input())):
    r,c = map(int,input().split())
    print(dp[r-1][c-1])