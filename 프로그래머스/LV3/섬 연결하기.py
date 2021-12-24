def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x:x[2])
    island = set([costs[0][0]])
    while len(island)!=n:
        for i in costs:
            print(island,answer)
            if i[0] in island and i[1] in island:
                continue
            if i[0] in island or i[1] in island:
                island.update([i[0],i[1]])
                answer += i[2]
                break
    return answer
solution(4,[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]])
solution(5,[[0, 1, 1], [3, 1, 1], [0, 2, 2], [0, 3, 2], [0, 4, 100]])