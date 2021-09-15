def solution(absolutes, signs):
    for i,v in enumerate(signs):
        if v == False:
            absolutes[i] *= -1
    print(absolutes)
    answer = 1234567
    answer = sum(absolutes)
    print(answer)
    return answer
solution([4,7,12],	[True,False,True])