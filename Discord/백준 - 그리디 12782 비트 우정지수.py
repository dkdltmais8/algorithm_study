n = int(input())
for i in range(n):
    a,b = map(str,input().split())
    zero,one = 0,0
    for j in range(len(a)):
        if a[j] == b[j]: continue
        if b[j] == '0':
            zero += 1
        else:
            one += 1
    # 다른 것중에 작은 만큼 바꿔주고 나머지는 위치 변경
    cnt = min(zero,one)
    #다른 만큼 바꿔주고 안바꿔줘도 되는 부분을 뺴준다.
    print(zero+one-cnt)