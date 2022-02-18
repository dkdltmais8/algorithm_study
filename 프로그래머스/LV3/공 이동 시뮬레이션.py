def solution(n, m, x, y, queries):
    sr,sc = x,y
    er,ec = x,y
    for i,v in queries[::-1]:
        if i == 0:
            if sc != 0:
                sc += v
                if sc>m-1:
                    sc = m-1
            ec += v
            if ec > m-1:
                ec = m-1

solution(2,2,0,0,[[2,1],[0,1],[1,1],[0,1],[2,1]])