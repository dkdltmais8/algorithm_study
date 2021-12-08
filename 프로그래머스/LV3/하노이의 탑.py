def solution(n):
    def move(start,end,middle,n):
        nonlocal answer
        print(answer,n)
        if n == 1:
            return answer.append([start,end]) #start에 있는 제일 큰 것을 end로 옮긴다.
        move(start,middle,end,n-1) #end를 거쳐 start를 middel로 옮긴다
        print(answer, n)
        answer.append([start,end]) #이동 기록
        move(middle,end,start,n-1) #start를 거쳐 middle 에서 end로 옮긴다.
    answer = []
    move(1,3,2,n)
    print(answer)
    return answer
solution(3)