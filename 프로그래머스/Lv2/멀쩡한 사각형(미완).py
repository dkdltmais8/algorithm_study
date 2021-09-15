import math as m
def solution(w,h):
    answer = 0
    #기울기 1
    if w == h:
        #전체에서 대각선의 개수만 뺴주면 됨
        return w*h-w
    # 모든 칸이 대각선 안에 포함
    elif w == 1 or h == 1:
        return 0
    for x in range(1,w):
        y = m.ceil((h/w)*x)
        answer += h-y
        print(x,y,answer)
    return answer
solution(8,12)