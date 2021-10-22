def solution(x):
    answer = True
    x = str(x)
    tot = 0
    for i  in x:
        tot+=int(i)
    x=int(x)
    if x%tot!=0:
        answer=False
    return answer