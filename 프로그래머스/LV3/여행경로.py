def solution(tickets):
    def dfs(now):
        if len(tickets)==0:
            return answer
        for i,v in enumerate(tickets):
            if now == v[0]:
                next = v[1]
                tickets.pop(i)
                answer.append(next)
                
    answer = ['ICN']
    tickets.sort()
    print(tickets)
    dfs("ICN")

    return answer
solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]])
solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"],
          ["ATL", "ICN"], ["ATL","SFO"]])
