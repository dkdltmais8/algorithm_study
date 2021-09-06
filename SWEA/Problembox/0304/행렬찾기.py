# def search(r,c):
#     r_cnt = 0
#     c_cnt = 0
#     for i in range(r,n):
#         if board[i][c] != 0:
#             r_cnt += 1
#         else:
#             break
#     for i in range(c,n):
#         if board[r][i] != 0:
#             c_cnt += 1
#         else:
#             break
#     ans.append([r_cnt, c_cnt, r_cnt*c_cnt])
#     init(r,c,r_cnt,c_cnt)
# def init(r,c,r_cnt,c_cnt):
#     for i in range(r,r+r_cnt):
#         for j in range(c,c+c_cnt):
#             board[i][j] = 0
# def counting_sort(idx):
#     cnt = [0]*10001
#     sort_ans = [0]*len(ans)
#
#     for i in range(len(ans)):
#         cnt[ans[i][idx]] += 1
#     for i in range(1,len(cnt)):
#         cnt[i] += cnt[i-1]
#     for i in range(len(ans)-1,-1,-1):
#         sort_ans[cnt[ans[i][idx]]-1] = ans[i]
#         cnt[ans[i][idx]] -= 1
#     return sort_ans
#
# T = int(input())
# for tc in range(1, T+1):
#     n = int(input())
#     board = [list(map(int,input().split())) for _ in range(n)]
#     ans = []
#     for i in range(n):
#         for j in range(n):
#             if board[i][j] != 0:
#                 search(i,j)
#     ans = counting_sort(0)
#     ans = counting_sort(2)
#     print("#{} {}".format(tc,len(ans)), end= " ")
#     for i in range(len(ans)):
#         print("{} {}".format(ans[i][0], ans[i][1]),end = " ")
#     print()


## 넓이, 높이 쉽게 구하기
T = int(input())
for tc in range(1, T+1):
    n = int(input())
    board = [list(map(int,input().split())) for _ in range(n)]
    ans = []
    for i in range(n):
        for j in range(n):
            if board[i][j] != 0:
                r = i
                while r< n and board[r][j]:
                    c = j
                    while c< n and board[r][c]:
                        board[r][c] = 0
                        c += 1
                    r += 1
                ans.append([r-i, c-j])
