def solution(tickets):
    def dfs(now):
        for i,v in enumerate(tickets):
            if now == v[0] and not visit[i]:
                answer.append(v[1])
                visit[i] = 1
                dfs(v[1])
                if len(answer) == len(tickets) + 1:
                    return
                visit[i] = 0
                answer.pop()
    answer = ['ICN']
    tickets.sort()
    visit = [0]*len(tickets)
    dfs('ICN')
    print(answer)
    return answer
solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]])
solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"],
          ["ATL", "ICN"], ["ATL","SFO"]])
solution([["ICN", "B"], ["B", "ICN"], ["ICN", "A"], ["A", "D"], ["D", "A"]])