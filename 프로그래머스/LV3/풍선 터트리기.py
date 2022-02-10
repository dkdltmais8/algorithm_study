def solution(a):
    answer = 0
    flag = [0]*len(a)
    s,e = float('inf'),float('inf')
    for i in range(len(a)):
        #양 끝점을 제외하고 반복하고 마지막에 남으면 크든 작든 가능하기 때문
        #양 끝점은 무조건 가능하기 때문에 처음에 무조건 적용
        #현재 값이 기존 제일 작은 값보다 작다면 가능한 값이다.
        if a[i]<s:
            flag[i] = 1
            s = a[i]
        #현재 값이 기존 제일 작은 값보다 작다면 가능한 값이다.
        if a[-1-i]< e:
            flag[-1-i] = 1
            e = a[-1-i]
    print(flag)
    #flag에서 가능한 개수만큼 출력
    return flag.count(1)
solution([9,-1,-5])