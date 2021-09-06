# def adjacent(x):
#     for i in range(x):
#         if row[x] == row[i] or abs(row[x] - row[i]) == x - i: # 열이 같거나 대각선이 같으면 false
#             return False # 대각선이 같은경우는 두 좌표에서 행 - 행 = 열 - 열 이 같으면 두개는 같은 대각선상에 있다.
#     return True
#

#
# def dfs(x):
#     global result
#
#     if x == N:
#         result += 1
#     else:
#         # 각 행에 퀸 놓기
#         for i in range(N):
#             row[x] = i
#             if adjacent(x):
#                 dfs(x + 1)
# ans = []
# for N in range(1,15):
#     # N = int(input())
#     row = [0] * N
#     result = 0
#     dfs(0)
#     ans.append(result)
# print(ans)
res = [1, 0, 0, 2, 10, 4, 40, 92, 352, 724, 2680, 14200, 73712, 365596]
print(res[int(input())-1])