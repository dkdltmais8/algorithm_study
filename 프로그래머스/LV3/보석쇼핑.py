from collections import defaultdict
def solution(gems):
    answer = [1,len(gems)+1]
    dict = defaultdict(int)
    num = len(set(gems))
    l,r = 0,0
    while r < len(gems):
        dict[gems[r]] += 1
        r += 1
        if len(dict) == num:
            while l < r:
                if dict[gems[l]] <= 1:
                    break
                dict[gems[l]] -= 1
                l += 1
            if answer[1]-answer[0]+1>r - l:
                answer = [l+1,r]
    print(dict)
    print(answer)
    return answer
solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"])