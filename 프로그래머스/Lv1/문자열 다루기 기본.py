def solution(s):
    answer = True
    if len(s)!=4 and len(s)!=6:
        answer=False
    s = list(s)
    for i in s:
        if i.isalpha():
            answer = False
    print(answer)
    return answer
solution("a234")
solution("1234")