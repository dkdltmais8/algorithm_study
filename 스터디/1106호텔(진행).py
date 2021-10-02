from sys import maxsize
# c => 최소 증가 인원
# n => 도시 개수
# def cal(c,n):
#     lst = [0]*2001
#     ans = 101*n
#     if c <=0:
#         return 0
#     elif lst[c] > 0:
#         return lst[c]
#     else:
#         for i in  range(n):
#             cost = cal(c-arr[i][1],n)+arr[i][0]
#             ans = cost if cost < ans else ans
#         lst[c] = ans
#         return ans
# c, n = map(int,input().split())
# arr = [list(map(int,input().split())) for _ in range(n)]
# ans = 0
# res = cal(c,n)
# print(res)

##효율은 좋지만 최소인원보다 수가 작으면 실행 자체를 시킬 수 없음
# https://www.acmicpc.net/problem/1106


c, n = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
dp = [0]+[maxsize]*(c+100)
for cost,people in arr:
    for person in range(people,c+101):
        dp[person] = min(dp[person],dp[person-people]+cost)
print(min(dp[c:]))