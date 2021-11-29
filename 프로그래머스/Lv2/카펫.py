def solution(brown, yellow):
    answer = []
    tot = brown+yellow
    for i in range(1,yellow+1):
        if yellow%i==0:
            mok = yellow // i
            if (mok+2)*(i+2) == tot:
                answer.append(mok+2)
                answer.append(i+2)
                break
    # print(answer)
    return answer
solution(10,2)
solution(8,1)
solution(24,24)