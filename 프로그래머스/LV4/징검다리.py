def solution(distance, rocks, n):
    answer = 0
    l,r = 0,distance
    rocks.sort()
    while l<=r:
        mid = (l+r)//2
        #제거한 돌
        cnt = 0
        #시작 지점
        start = 0
        for rock in rocks:
            #돌 사이 거리가 가정한 값보다 작으면 제거
            if rock - start < mid:
                cnt += 1
            #가정 값보다 같거나 크면 시작점 바꿔줌
            else:
                start = rock
            #실패할 루틴
            if cnt>n:
                break
        #제거된 돌이 많으면 가정값이 큰 것이니까 기준을 줄여준다.
        if cnt > n:
            r = mid-1
        #제거된 돌이 같거나 적으면 너무 작은거니까 범위를 크게해준다.
        else:
            answer = mid
            l = mid+1
    return answer
solution(25,[2, 14, 11, 21, 17],2)