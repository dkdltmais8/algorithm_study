# for i in range(10):
#     N = int(input())
#     T = []
#     for col in range(8):
#         T.append(input())
#     T =list("".join(T))
#     cnt = 0
#     for j in range(8):
#         for k in range(1,10-N):
#             a = T[k-1:(k + 3)]
#             if a == a[::-1]:
#                 cnt += 1
#     for j in range(1,9):
#         for k in range(9-N):
#             b = T[k * 8: ((N - k + 1) * 8) + 1: 8]
#             if b == b[::-1]:
#                 cnt += 1
#     print(f'#{i+1} {cnt}')

# D3 1215 회문1
def check(a):
    l = len(a)
    for i in range(l // 2):
        if a[i] != a[l - i - 1]:
            return False
    return True


T = 10
for t in range(1, T + 1):
    length = int(input())
    map_list = []
    map_list2 = []
    N = 8
    for i in range(N):
        map_list.append(input())
    for i in range(N):
        str_temp = ''
        for k in range(N):
            str_temp += map_list[k][i]

        map_list2.append(str_temp)

    result = 0
    for i in range(N):
        for j in range(N - length + 1):
            if check(map_list[i][j:j + length]):
                result += 1
            if check(map_list2[i][j:j + length]):
                result += 1

    print("#{} {}".format(t, result))

# for test_case in range(1,11):
#     answer = 0
#     length = int(input())
#     array = [list(input().strip()) for _ in range(8)]

#     trans_array = list(map(list, zip(*array)))

#     for i in range(8):
#         for j in range(9 - length):
#             garo = array[i][j:j + length]
#             sero = trans_array[i][j:j + length]

#             if garo == garo[::-1]:
#                 answer += 1

#             if sero == sero[::-1]:
#                 answer += 1

#     print('#' + str(test_case), answer)