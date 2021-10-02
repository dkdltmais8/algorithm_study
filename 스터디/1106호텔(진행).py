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

from sys import maxsize
# c<=1000
c, n = map(int,input().split())
#arr의 값 <= 100
arr = [list(map(int,input().split())) for _ in range(n)]
#최소값을 넣기 위해 제일 큰 숫자들로 채워진 c+101크기의 리스트를 만듦
dp = [0]+[maxsize]*(c+100)
# 도시를 돌면서 비교
for cost,people in arr:
    #c는 최소인원이고 만약 각 도시에서 한번에 불러오는 인구 자체가 클 수 있으므로 최대치인 100만큼 더 계산해준다
    for person in range(people,c+101):
        #dp를 돌면서 각각 인원 인덱스의 배수에 비용을 넣어주고 도시간의 비교도 자동으로 실행
        # 고객수에 맞는 인덱스에 비용을 넣고, 현재의 비용과 지금 진행했을 때의 비용을 비교해서 적은걸 넣어줌
        dp[person] = min(dp[person],dp[person-people]+cost)
print(min(dp[c:]))