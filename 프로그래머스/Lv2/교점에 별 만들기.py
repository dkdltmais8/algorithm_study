def solution(line):
    INF = float('inf')
    point = []
    n = len(line)
    minx,maxx,miny,maxy = INF,-INF,INF,-INF
    for i in range(n):
        for j in range(i,n):
            if i == j:
                continue
            a,b,e,c,d,f = *line[i], *line[j]
            k = a*d-b*c
            if k == 0:
                continue
            x,y = (b*f-e*d)/k,(e*c-a*f)/k
            if (not x.is_integer()) or (not y.is_integer()):
                continue
            x,y = int(x),int(y)
            minx,maxx,miny,maxy = min(minx,x),max(maxx,x),min(miny,y),max(maxy,y)
            point.append((x,y))
    board = [['.' for _ in range(maxx-minx+1)] for _ in range(maxy-miny+1)]
    for x,y in point:
        board[maxy-y][x-minx] = '*'
    return [''.join(i) for i in board]
solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]])