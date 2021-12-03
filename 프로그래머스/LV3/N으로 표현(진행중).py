def solution(N, number):
    answer = 0
    ans = []
    temp = number
    while number>0:
        number-=N
        answer +=1
        if number<0:
            number+=N
            answer-=1
            answer+= 2*number
            number = 0
    ans.append(answer)
    if number != 0:
        number = temp
        answer = 0
    
    print(ans,answer)
    return answer
solution(5,12)
solution(2,11)