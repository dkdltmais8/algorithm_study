def solution(numbers):
    answer = ''
    ans = []
    for i in numbers:
        fake = (str(i)*4)[:4]
        real = len(str(i))
        ans.append((fake,real))
    ans.sort(reverse=True)
    for fake,real in ans:
        answer += fake[:real]
    answer = str(int(answer))
    return answer