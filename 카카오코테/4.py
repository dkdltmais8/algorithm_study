def solution(n, info):
    answer = []
    def dfs(n,lion,lion_tot,appeach,appeach_tot):
        if lion_tot > appeach_tot:
            answer.append(lion)
            return
        i = 10
        while sum(lion) < n:
            if appeach[i] >= lion[i]:
                lion[i] += 1
            else:
                i -= 1

    info = info[::-1]
    lion = [0,0,0,0,0,0,0,0,0,0,0]
    dfs(n,lion,0,info,0)
    print(lion)
    return answer
solution(5,[2,1,1,1,0,0,0,0,0,0,0])