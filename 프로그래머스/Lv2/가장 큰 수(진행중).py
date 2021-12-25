def solution(numbers):
    answer = ''
    d = len(numbers)
    res=[]
    for i in numbers:
        fake = (str(i)*4)[:4]
        real = len(str(i))
        res.append((fake,real))
    res.sort(reverse=True)
    for (fake,real) in res:
        answer += fake[:real]

    if answer != str(int(answer)):
        answer = '0'
    return answer
solution([3,30,34,5,9])
solution([6,10,2])