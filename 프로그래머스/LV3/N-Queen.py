def solution(n):
    def check(idx):
        for i in range(idx):
            if row[idx]==row[i] or abs(row[idx]-row[i]) ==idx-i:
                return False
        return True
    def  dfs(idx):
        nonlocal answer
        if idx == n:
            answer += 1
        else:
            for i in range(n):
                row[idx] = i
                if check(idx):
                    dfs(idx+1)
    answer = 0
    row = [0]*n
    dfs(0)
    # print(answer)
    return answer
solution(4)