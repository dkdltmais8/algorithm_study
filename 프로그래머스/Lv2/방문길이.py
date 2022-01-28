def solution(dirs):
    def move(dir):
        nonlocal answer,r,c
        nr,nc = r,c
        if dir == 'U':
            if r==20:
                return
            r+= 2
        elif dir == 'D':
            if r==0:
                return
            r -= 2
        elif dir == 'R':
            if c==20:
                return
            c += 2
        elif dir == 'L':
            if c==0:
                return
            c -= 2
        cr,cc = (nr+r)//2,(nc+c)//2
        visit[cr][cc] += 1
        if not (visit[cr][cc] > 1):
            answer += 1
        return
    answer = 0
    visit = [[0]*22 for _ in range(22)]
    r,c = 10,10
    for i in dirs:
        move(i)
    print(answer)
    return answer
solution("ULURRDLLU")
solution("LULLLLLLU")