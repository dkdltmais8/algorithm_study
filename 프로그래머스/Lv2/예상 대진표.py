def solution(n,a,b):
    answer = 1
    while 1:
        if a%2==0:
            if b == a-1:
                break
        if a%2:
            if b == a+1:
                break
        answer += 1
        a = (a+1)//2
        b = (b+1)//2
    # print(answer)
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    return answer
solution(8,4,7)
