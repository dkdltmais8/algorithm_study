def solution(a):
    answer = 0
    flag = [0]*len(a)
    s,e = float('inf'),float('inf')
    for i in range(len(a)):
        #양 끝점을 제외하고 반복하고 마지막에 남으면 크든 작든 가능하기 때문
        #양 끝점은 무조건 가능하기 때문에 처음에 무조건 적용
        if a[i]<s:
            flag[i] = 1
            s = a[i]
        if a[-1-i]< e:
            flag[-1-i] = 1
            e = a[-1-i]
    print(flag)
    return flag.count(1)
solution([9,-1,-5])