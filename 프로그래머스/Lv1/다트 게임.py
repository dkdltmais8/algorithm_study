def solution(dartResult):
    #스택이용
    score = []
    for i in dartResult:
        if i.isdigit():
            score.append(int(i))
            if len(score) >= 2:
                if score[-1] == 0 and score[-2] == 1:
                    score[-2] = 10
                    score.pop(-1)
        elif i.isalpha():
            if i == "S":
                score[-1] = score[-1] ** 1
            elif i == "D":
                score[-1] = score[-1] ** 2
            else:
                score[-1] = score[-1] ** 3
        else:
            if i == "*":
                if len(score) == 1:
                    score[-1] = score[-1] * 2
                else:
                    score[-1] = score[-1] * 2
                    score[-2] = score[-2] * 2
            else:
                score[-1] = score[-1] * (-1)

    return sum(score)
solution('1S2D*3T')
solution('1D2S#10S')
solution('1D2S0T')
solution('1S*2T*3S')