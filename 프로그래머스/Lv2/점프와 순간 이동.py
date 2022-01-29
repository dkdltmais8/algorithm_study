#한번에 k칸을 앞으로 점프 - 건전지 k만큼 소모
#현재깍지 온 거리*2에 해당위치로 순간이동 - 건전지 사용 x
def solution(n):
    answer = 1
    while n >1:
        if n%2:
            n-=1
            answer += 1
        n//=2
    return answer
solution(5)
solution(6)
solution(5000)