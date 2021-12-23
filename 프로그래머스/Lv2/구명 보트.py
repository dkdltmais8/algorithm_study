def solution(people, limit):
    answer = 0
    people.sort()
    i,j = 0,len(people)-1
    while i<=j:
            if i!=j and people[i]+people[j]<=limit:
                i += 1
                j -= 1
            else:
                j -= 1
            answer += 1
    return answer
solution([50,40,150,160],200)
solution([70, 50, 80, 50],100)