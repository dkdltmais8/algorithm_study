def solution(n, m, y, x, queries):
    sr = er = y
    sc= ec = x
    ans = 0
    for i,v in queries[::-1]:
        if i == 0:
            if sc != 0:
                sc += v
            ec += v
            if ec > m-1:
                ec = m-1
        elif i == 1:
            sc -= v
            if sc<0:
                sc = 0
            if ec !=m-1:
                ec-=v
        elif i == 2:
            if sr != 0:
                sr += v
            er += v
            if er >n-1:
                er = n-1
        elif i == 3:
            sr -= v
            if sr<0:
                sr = 0
            if er != n-1:
                er-=v
        if sr>n-1 or er<0 or sc>m-1 or ec<0:
            return ans
    return (er-sr+1) * (ec-sc+1)
print(solution(2,2,0,0,[[2,1],[0,1],[1,1],[0,1],[2,1]]))
print(solution(1000,1000,1,1,[[0,100001],[2,100001]]))