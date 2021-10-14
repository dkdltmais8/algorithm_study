def solution(sizes):
    # answer = 0
    sizes.sort()
    for i in sizes:
        if i[0] < i[1]:
            i[0],i[1] = i[1],i[0]
    # print(sizes)
    max_h,max_w = 0,0
    for i in sizes:
        if i[1] > max_h:
            max_h = i[1]
        if i[0] > max_w:
            max_w = i[0]
    answer = max_h*max_w
    return answer
solution([[60, 50], [30, 70], [60, 30], [80, 40]])
solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]])
solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]])
#
# 먼저는 가로의 길이와 세로의 길이에서 각각의 최댓값을 구해 두 값 중에 작은 값의 가로와 세로를 바꾸는 식으로 진행했는데 그렇게 하다 보니 중간 값들에서 문제가 발생했다.
#
# 그래서 아예 가로로 긴 직사각형 형태로 다 바꿔서 최댓값과 바꾼 후 세로의 최댓값을 곱해서 해결했다.
#
# 이것도 유연한 사고가 필요,,
